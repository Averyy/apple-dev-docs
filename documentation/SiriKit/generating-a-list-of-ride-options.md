# Generating a List of Ride Options

**Framework**: SiriKit

Generate ride options for Maps to display to the user.

#### Overview

When the user selects Ride as the transportation option, Maps sends an [`INListRideOptionsIntent`](https://developer.apple.com/documentation/intents/inlistrideoptionsintent) object to any Intents app extensions that support the intent. In your response to that intent, provide one or more [`INRideOption`](https://developer.apple.com/documentation/intents/inrideoption) objects representing the rides you’re able to offer. Keep your list of rides reasonably short and representative of the types of vehicles and price points that are available. Don’t return an exhaustive list of all vehicles available to pick up the user.

##### Include Essential Information

For each ride option, include as much information as possible about the ride, including its pricing, passenger capacity, disclaimers, and an estimated time at which a vehicle of that type could arrive at the user’s location. Make the information as accurate as possible, but understand that you can update the information when actually booking the ride. Here are some tips to creating your [`INRideOption`](https://developer.apple.com/documentation/intents/inrideoption) objects:

-  Ride option names should convey information about the ride type and be unique so that you can identify them later. When the user selects a ride option for booking, SiriKit passes only the option name back to you. So you must be able to identify the ride type from that string.
-  If the number of people receiving a ride determines the price, configure the [`availablePartySizeOptions`](https://developer.apple.com/documentation/intents/inrideoption/availablepartysizeoptions) and [`availablePartySizeOptionsSelectionPrompt`](https://developer.apple.com/documentation/intents/inrideoption/availablepartysizeoptionsselectionprompt) properties appropriately. Use your [`INRidePartySizeOption`](https://developer.apple.com/documentation/intents/inridepartysizeoption) objects to specify the pricing information for parties of different sizes.
-  When the cost of a ride isn’t a single fixed value, provide fare line items so that the user understands how the app computed the fare. Line items can include base charges, per-mile charges, additional fees or tolls, and discounts.
-  Expiration dates prevent your ride options from becoming stale or outdated. When a ride option expires, SiriKit sends another [`INListRideOptionsIntent`](https://developer.apple.com/documentation/intents/inlistrideoptionsintent) object to your Intents extension.
-  You might complete the booking in your app when special circumstances apply, such as when you need to change the precise pickup or drop-off location. Assigning an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object to the [`userActivityForBookingInApplication`](https://developer.apple.com/documentation/intents/inrideoption/useractivityforbookinginapplication) property of the [`INRideOption`](https://developer.apple.com/documentation/intents/inrideoption) tells Maps that it must launch your app to complete the booking.

The following figure shows how Maps reveals the party size details to the user. When selecting a vehicle, Maps displays the base price range initially. When the user actually requests the vehicle, Maps prompts the user to select the number of passengers. Base the information for each price tier on the information you supply in the [`INRidePartySizeOption`](https://developer.apple.com/documentation/intents/inridepartysizeoption) objects.

![A screenshot that shows a list of ride options with the title “Choose a party size”. The list offers ride options for 1 person, 2-3 people, and 4+ people, with prices. Behind the list is a dimmed view that includes the ride’s destination, type of vehicle, and other information.](https://docs-assets.developer.apple.com/published/c5fa03312ee554806b0e5aa23aceee92/media-3866871%402x.png)

##### Create Ride Options

The following code shows the creation of an [`INRideOption`](https://developer.apple.com/documentation/intents/inrideoption) object for a compact car with fixed pricing options. In this case, the ride-booking service computes the price of the ride and quotes it directly. Because the ride’s price and number of passengers can’t change, it includes a disclaimer message to convey the vehicle capacity rather than assigning a value to the [`availablePartySizeOptions`](https://developer.apple.com/documentation/intents/inrideoption/availablepartysizeoptions) property.

```swift
func createCompactRideOption(pickup : CLPlacemark, 
                            dropOff : CLPlacemark ) -> INRideOption  {   
   let ride = INRideOption(name: "Compact",
		          estimatedPickupDate: self.getCompactEstimatedPickupTime()) 
   ride.disclaimerMessage = "Vehicle can carry only 1 passenger."
		    
	// Compacts have a fixed charge based on the distance.
	let charges = self.computeCompactCharges(pickup: pickup, dropOff: dropOff)
	ride.priceRange = INPriceRange(price: NSDecimalNumber(value : charges),
		                                   currencyCode: "USD")
	return ride
}
```

The following code shows another example of how to create an [`INRideOption`](https://developer.apple.com/documentation/intents/inrideoption), in this case for an SUV type of vehicle. In this case, there are three separate pricing tiers according to the number of passengers. Each tier requires a separate [`INRidePartySizeOption`](https://developer.apple.com/documentation/intents/inridepartysizeoption) object to include the pricing and information about the number of passengers. The ride option also fills in the [`priceRange`](https://developer.apple.com/documentation/intents/inrideoption/pricerange) property based on the prices of the different configurations.

```swift
func createSUVRideOption(pickup : CLPlacemark, 
                        dropOff : CLPlacemark ) -> INRideOption {
   let ride = INRideOption(name: "SUV",
		   estimatedPickupDate: self.getSUVEstimatedPickupTime())
		    
   // Configure party size options.
		    
   let baseCharge = self.getBaseCharge()
	let perMileCharge = self.getPerMileCharge()
	let suvSurcharge = self.getSUVSurcharge()
	let extraPersonSurcharge = self.getExtraPersonSurcharge()
		    
	// Compute the base prices for one person.
	let (rideDistance, tollCharges) = self.computeRouteDistanceAndTolls(pickup: pickup,
		                                                                dropOff: dropOff)
	let distanceCost = perMileCharge * rideDistance
	let minimumCost = distanceCost + baseCharge + suvSurcharge + tollCharges
		    
	// Configure the one-person party size.
	let onePersonPriceRange = INPriceRange(price: NSDecimalNumber(value : minimumCost),
		                                           currencyCode: "USD")
	let onePersonParty = INRidePartySizeOption(partySizeRange: NSMakeRange(0, 1),
		               sizeDescription: "1 person", priceRange: onePersonPriceRange)
		    
	// Configure the 2-3 person party size.
	let threePersonPriceRange = INPriceRange(price: NSDecimalNumber(value : minimumCost +
		        extraPersonSurcharge), currencyCode: "USD")
	let threePersonParty = INRidePartySizeOption(partySizeRange: NSMakeRange(2, 1),
		               sizeDescription: "2-3 people", priceRange: threePersonPriceRange)
		    
	// Configure the 4+ person party size.
	let fourPersonPriceRange = INPriceRange(price: NSDecimalNumber(value : minimumCost +
		        (2 * extraPersonSurcharge)), currencyCode: "USD")
	let fourPersonParty = INRidePartySizeOption(partySizeRange: NSMakeRange(4, 3),
		               sizeDescription: "4+ people", priceRange: fourPersonPriceRange)
		    
	// Configure the party size options
	ride.availablePartySizeOptions = [onePersonParty, threePersonParty, fourPersonParty]
	ride.availablePartySizeOptionsSelectionPrompt = "Choose a party size"
	ride.priceRange = INPriceRange(firstPrice: NSDecimalNumber(value : minimumCost),
		               secondPrice: NSDecimalNumber(value : minimumCost + 
                           (2 * extraPersonSurcharge)), currencyCode: "USD")
		    
	return ride
}
```

## See Also

- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Dispatching intents to handlers](dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](improving-siri-media-interactions-and-app-selection.md)
  Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Improving interactions between Siri and your messaging app](improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](confirming-the-details-of-an-intent.md)
  Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](handling-an-intent.md)
  Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](resolving-the-parameters-of-an-intent.md)
  Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Handling the Ride-Booking Intents](handling-the-ride-booking-intents.md)
  Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/generating-a-list-of-ride-options)*