# init(defaultPartySize:defaultBooking:code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified information and user activity object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(defaultPartySize: Int, defaultBooking defaultBookingDate: Date, code: INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithDefaultPartySize:(NSUInteger) defaultPartySize defaultBookingDate:(NSDate *) defaultBookingDate code:(INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

#### Return Value

An initialized response object or `nil` if the object could not be created.

## Parameters

- `defaultPartySize`: The default size of the user’s party. The value should reflect a reasonable estimate of the number of people the user is likely to have in their party and should be between the restaurant’s stated minimum and maximum values.
- `defaultBookingDate`: The default booking date to display to the user. This date should reflect a reasonable estimate of the time that the user might want for a reservation, taking into account the current availability of reservations at the given restaurant.
- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode`](../ingetavailablerestaurantreservationbookingdefaultsintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add information that is specific to your app. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse/init(defaultpartysize:defaultbooking:code:useractivity:))*