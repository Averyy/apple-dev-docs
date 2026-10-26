# reservationDuration

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time range that defines beginning and end of the restaurant reservation.

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
var reservationDuration: INDateComponentsRange { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INDateComponentsRange * reservationDuration;
```

*macOS*

```objc
@property (atomic, copy, readonly) INDateComponentsRange * reservationDuration;
```

## See Also

### Getting the Restaurant Reservation Information
- [var restaurantLocation: CLPlacemark](./restaurantlocation.md)
  The name and location of the restaurant.
- [var partySize: Int?](./partysize-9ux0p.md)
  The number of people in the party.
- [partySize](./partysize-9mtpk.md)
  The number of people in the party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation/reservationduration)*