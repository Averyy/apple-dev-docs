# userCurrentBookings

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of the user’s current reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var userCurrentBookings: [INRestaurantReservationUserBooking] { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSArray<INRestaurantReservationUserBooking *> * userCurrentBookings;
```

*macOS*

```objc
@property (atomic, copy) NSArray<INRestaurantReservationUserBooking *> * userCurrentBookings;
```

## Discussion

During the handling phase of the intent, your handler object should put the user’s reservations in this property. If there are no outstanding reservations associated with the user and matching the criteria in the intent object, specify an empty array for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponse/usercurrentbookings)*