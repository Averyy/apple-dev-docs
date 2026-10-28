# reservationIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An identifier to use when searching for the user’s reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var reservationIdentifier: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * reservationIdentifier;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * reservationIdentifier;
```

## Discussion

When the system wants to display a specific reservation, this property contains the identifier for that reservation. Use this identifier to fetch only the specified reservation. When this property is `nil`, return all of the user’s current reservations, or those specific to the restaurant listed in the [`restaurant`](./restaurant.md) property.

## See Also

### Getting the Search Parameters
- [var restaurant: INRestaurant?](./restaurant.md)
  A restaurant to use as a filter when searching for reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent/reservationidentifier)*