# restaurant

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A restaurant to use as a filter when searching for reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var restaurant: INRestaurant? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurant * restaurant;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurant * restaurant;
```

#### Discussion

Use the restaurant information in this property as a filter when searching for the user’s current reservations. Associate any reservation you return with the specified restaurant If this property is `nil`, your search results can include reservations at any restaurant.

## See Also

### Getting the Search Parameters
- [var reservationIdentifier: String?](./reservationidentifier.md)
  An identifier to use when searching for the user’s reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent/restaurant)*