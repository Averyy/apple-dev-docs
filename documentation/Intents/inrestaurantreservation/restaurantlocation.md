# restaurantLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name and location of the restaurant.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var restaurantLocation: CLPlacemark { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CLPlacemark * restaurantLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly) CLPlacemark * restaurantLocation;
```

## See Also

### Getting the Restaurant Reservation Information
- [var reservationDuration: INDateComponentsRange](./reservationduration.md)
  The date and time range that defines beginning and end of the restaurant reservation.
- [var partySize: Int?](./partysize-9ux0p.md)
  The number of people in the party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation/restaurantlocation)*