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

## Discussion

Use this object to determine the restaurant at which to create the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent/restaurant)*