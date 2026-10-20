# MKUserTrackingMode.followWithHeading

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

The map follows the user’s location and rotates when the heading changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case followWithHeading
```

```c
MKUserTrackingModeFollowWithHeading
```

#### Discussion

This mode requires the device to have an available magnetometer. This mode isn’t available for compatible iPad or iPhone apps running in visionOS.

## See Also

### Constants
- [MKUserTrackingMode.none](./none.md)
  The map doesn’t follow the user’s location.
- [MKUserTrackingMode.follow](./follow.md)
  The map follows the user location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkusertrackingmode/followwithheading)*