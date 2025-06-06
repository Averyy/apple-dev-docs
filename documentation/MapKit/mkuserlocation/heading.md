# heading

**Framework**: MapKit  
**Kind**: property

The heading of the user’s location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
var heading: CLHeading? { get }
```

#### Discussion

This property is `nil` if the user’s location tracking mode isn’t [`MKUserTrackingMode.followWithHeading`](mkusertrackingmode/followwithheading.md).

## See Also

- [var location: CLLocation?](mkuserlocation/location.md)
  The location of the device.
- [var isUpdating: Bool](mkuserlocation/isupdating.md)
  A Boolean value that indicates whether the map view is updating the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkuserlocation/heading)*