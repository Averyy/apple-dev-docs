# ARConfiguration.WorldAlignment.gravityAndHeading

**Framework**: ARKit  
**Kind**: case

The coordinate system’s y-axis is parallel to gravity, its x- and z-axes are oriented to compass heading, and its origin is the initial position of the device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case gravityAndHeading
```

#### Discussion

The y-axis matches the direction of gravity as detected by the device’s motion sensing hardware; that is, the vector `(0,-1,0)` points downward.

The x- and z-axes match the longitude and latitude directions as measured by Location Services. The vector `(0,0,-1)` points to true north and the vector `(-1,0,0)` points west. (That is, the positive x-, y-, and z-axes point east, up, and south, respectively.)

![None](https://docs-assets.developer.apple.com/published/43ed9c7be6301ec1d30c268015670bf6/media-2891462%402x.png)

Although this option fixes the  of the three coordinate axes to real-world directions, the  of the coordinate system’s origin is still relative to the device, matching the device’s position as of when the session configuration is first run.

> **Note**:  Using gravity and heading alignment requires tracking the device’s geographic location. Your app’s Info.plist must include user-facing text for the [`NSLocationUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSLocationUsageDescription) or [`NSLocationWhenInUseUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSLocationWhenInUseUsageDescription) key so that the user can grant your app permission for location tracking.

## See Also

- [ARConfiguration.WorldAlignment.gravity](arconfiguration/worldalignment-swift.enum/gravity.md)
  The coordinate system’s y-axis is parallel to gravity, and its origin is the initial position of the device.
- [ARConfiguration.WorldAlignment.camera](arconfiguration/worldalignment-swift.enum/camera.md)
  The scene coordinate system is locked to match the orientation of the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.enum/gravityandheading)*