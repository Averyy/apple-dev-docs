# ARConfiguration.WorldAlignment.gravity

**Framework**: ARKit  
**Kind**: case

The coordinate system’s y-axis is parallel to gravity, and its origin is the initial position of the device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case gravity
```

#### Discussion

The y-axis matches the direction of gravity as detected by the device’s motion sensing hardware; that is, the vector `(0,-1,0)` points downward.

The position and orientation of the device as of when the session configuration is first run determine the rest of the coordinate system: For the z-axis, ARKit chooses a basis vector `(0,0,-1)` pointing in the direction the device camera faces and perpendicular to the gravity axis. ARKit chooses a x-axis based on the z- and y-axes using the right hand rule—that is, the basis vector `(1,0,0)` is orthogonal to the other two axes, and (for a viewer looking in the negative-z direction) points toward the right.

![None](https://docs-assets.developer.apple.com/published/8e9847c4e7859da69ad7cbda0ca2192f/media-2891463%402x.png)

## See Also

- [ARConfiguration.WorldAlignment.gravityAndHeading](arconfiguration/worldalignment-swift.enum/gravityandheading.md)
  The coordinate system’s y-axis is parallel to gravity, its x- and z-axes are oriented to compass heading, and its origin is the initial position of the device.
- [ARConfiguration.WorldAlignment.camera](arconfiguration/worldalignment-swift.enum/camera.md)
  The scene coordinate system is locked to match the orientation of the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.enum/gravity)*