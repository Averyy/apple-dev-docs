# lodgingBusinessLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name and location of the lodging establishment.

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
var lodgingBusinessLocation: CLPlacemark { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CLPlacemark * lodgingBusinessLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly) CLPlacemark * lodgingBusinessLocation;
```

## See Also

### Getting the Lodging Reservation Information
- [var reservationDuration: INDateComponentsRange](./reservationduration.md)
  The date and time range that indicates the beginning and end of the reservation.
- [var numberOfAdults: Int?](./numberofadults-6fsnq.md)
  The number of adults staying at the lodging location.
- [var numberOfChildren: Int?](./numberofchildren-1dm3g.md)
  The number of children staying at the lodging location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation/lodgingbusinesslocation)*