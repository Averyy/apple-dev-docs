# INRideOption

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Details about a type of ride offered by your ride-booking service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class INRideOption
```

```objc
@interface INRideOption : NSObject
```

## Mentions

- [Generating a List of Ride Options](../SiriKit/generating-a-list-of-ride-options.md)

#### Overview

When the user books a ride through Siri or Maps, you use [`INRideOption`](./inrideoption.md) objects to convey information about pricing and passenger capacity for that ride. Prior to booking, Maps asks for ride option objects representing the rides that are available from your service at that moment. Siri and Maps present ride option information to the user in appropriate contexts so that the user has information about potential rides.

You create [`INRideOption`](./inrideoption.md) objects in response to ride requests and when providing the user with a list of available rides. Always fill in as many properties of ride option objects as makes sense for that ride. Ride options let you specify pricing in several different ways, including as a range of values or as a set of line-item costs. You can also specify information about any special pricing that applies to the ride right now. After configuring the ride option, deliver it with the response object you return back to SiriKit.

## Topics

### Initializing a Ride Option
- [init(name: String, estimatedPickupDate: Date)](./inrideoption/init%28name,estimatedpickupdate%29.md)
  Initializes and returns a ride option object with the specified name and pickup information.
- [init?(coder: NSCoder)](./inrideoption/init%28coder%29.md)
### Specifying the Ride Information
- [var name: String](./inrideoption/name.md)
  The name of this ride option.
- [var estimatedPickupDate: Date](./inrideoption/estimatedpickupdate.md)
  The date and time when a ride of this type could be at the user’s location.
- [var disclaimerMessage: String?](./inrideoption/disclaimermessage.md)
  A localized disclaimer message to display to the user before confirming the ride.
- [var availablePartySizeOptions: [INRidePartySizeOption]?](./inrideoption/availablepartysizeoptions.md)
  An array of size options for the user to choose from.
- [var availablePartySizeOptionsSelectionPrompt: String?](./inrideoption/availablepartysizeoptionsselectionprompt.md)
  The localized text to display for selecting party size options.
### Specifying Pricing Information
- [var priceRange: INPriceRange?](./inrideoption/pricerange.md)
  The range of prices for this ride option.
- [var specialPricing: String?](./inrideoption/specialpricing.md)
  A user-visible string describing any special pricing considerations that apply to this ride.
- [var specialPricingBadgeImage: INImage?](./inrideoption/specialpricingbadgeimage.md)
  A template image for Maps to display when special prices apply.
- [var usesMeteredFare: Bool?](./inrideoption/usesmeteredfare-1sig1.md)
  A Boolean value indicating whether the price uses a metered fare instead of a fixed price.
- [var fareLineItems: [INRideFareLineItem]?](./inrideoption/farelineitems.md)
  An array of price-related items that break down the costs of the ride.
### Identifying the Ride Option
- [var identifier: String?](./inrideoption/identifier.md)
  A unique identifier for the ride option.
### Launching Your App
- [var userActivityForBookingInApplication: NSUserActivity?](./inrideoption/useractivityforbookinginapplication.md)
  A user activity object that you can use to launch the app.
### Instance Properties
- [var usesMeteredFare: NSNumber?](./inrideoption/usesmeteredfare-2xw1.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [class INRideStatus](./inridestatus.md)
  The status of a ride booked through a ride-booking service.
- [class INRideDriver](./inridedriver.md)
  Identifying information about a driver of a ride service.
- [class INRideVehicle](./inridevehicle.md)
  A specific vehicle used by a ride-booking service.
- [class INRideFareLineItem](./inridefarelineitem.md)
  A specific type of ride-related charge.
- [class INRidePartySizeOption](./inridepartysizeoption.md)
  The price of a ride involving the specified number of people.
- [class INRideCompletionStatus](./inridecompletionstatus.md)
  Additional details about whether a ride completed successfully or someone canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption)*