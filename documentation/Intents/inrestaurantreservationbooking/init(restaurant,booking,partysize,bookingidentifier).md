# init(restaurant:booking:partySize:bookingIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the reservation object with the specified information and status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(restaurant: INRestaurant, booking bookingDate: Date, partySize: Int, bookingIdentifier: String)
```

```objc
- (instancetype) initWithRestaurant:(INRestaurant *) restaurant bookingDate:(NSDate *) bookingDate partySize:(NSUInteger) partySize bookingIdentifier:(NSString *) bookingIdentifier;
```

## Return Value

An initialized reservation booking object or `nil` if the object could not be created.

## Discussion

After initializing the reservation booking object, update the other properties of the object with details about special offers or the requirements for completing the reservation.

## Parameters

- `restaurant`: The restaurant at which the reservation is to be made.
- `bookingDate`: The date and time of the reservation.
- `partySize`: The number of guests in the party.
- `bookingIdentifier`: The unique identifier for the reservation in your system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/init(restaurant:booking:partysize:bookingidentifier:))*