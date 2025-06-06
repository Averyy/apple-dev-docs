# CLLocationDistanceMax

**Framework**: Core Location  
**Kind**: var

A constant indicating the maximum distance.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CLLocationDistanceMax: CLLocationDistance
```

#### Discussion

When scheduling deferred updates, you can use this constant to indicate that a new update should be triggered only after the device moves a significantly large distance.

## See Also

- [var distanceFilter: CLLocationDistance](cllocationmanager/distancefilter.md)
  The minimum distance in meters the device must move horizontally before an update event is generated.
- [let kCLDistanceFilterNone: CLLocationDistance](kcldistancefilternone.md)
  A constant indicating that all movement should be reported.
- [typealias CLLocationDistance](cllocationdistance.md)
  A distance in meters from an existing location.
- [var desiredAccuracy: CLLocationAccuracy](cllocationmanager/desiredaccuracy.md)
  The accuracy of the location data that your app wants to receive.
- [typealias CLLocationAccuracy](cllocationaccuracy.md)
  The accuracy of a geographical coordinate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationdistancemax)*