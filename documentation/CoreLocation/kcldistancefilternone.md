# kCLDistanceFilterNone

**Framework**: Core Location  
**Kind**: var

A constant indicating that all movement should be reported.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCLDistanceFilterNone: CLLocationDistance
```

#### Discussion

Use this constant to specify that any change in location should trigger a new location update.

## See Also

- [var distanceFilter: CLLocationDistance](cllocationmanager/distancefilter.md)
  The minimum distance in meters the device must move horizontally before an update event is generated.
- [let CLLocationDistanceMax: CLLocationDistance](cllocationdistancemax.md)
  A constant indicating the maximum distance.
- [typealias CLLocationDistance](cllocationdistance.md)
  A distance in meters from an existing location.
- [var desiredAccuracy: CLLocationAccuracy](cllocationmanager/desiredaccuracy.md)
  The accuracy of the location data that your app wants to receive.
- [typealias CLLocationAccuracy](cllocationaccuracy.md)
  The accuracy of a geographical coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/kcldistancefilternone)*