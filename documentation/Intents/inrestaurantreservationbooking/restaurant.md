# restaurant

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The restaurant associated with the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var restaurant: INRestaurant { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) INRestaurant * restaurant;
```

*macOS*

```objc
@property (atomic, copy) INRestaurant * restaurant;
```

#### Discussion

This property must contain a valid restaurant object.

## See Also

### Accessing the Reservation Information
- [var partySize: Int](./partysize.md)
  The total number of guests in the party.
- [var offers: [INRestaurantOffer]?](./offers.md)
  An array of special offers from the restaurant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking/restaurant)*