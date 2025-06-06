# xMagneticNorthZVertical

**Framework**: Core Motion  
**Kind**: property

A reference frame where the Z axis is vertical and the X axis points to the magnetic north pole.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var xMagneticNorthZVertical: CMAttitudeReferenceFrame { get }
```

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Discussion

Use this option to determine the attitude of the device relative to magnetic north. For example, you might use this to implement a compass feature in your app. The [`yaw`](cmattitude/yaw.md) (Z-axis) value in [`CMAttitude`](cmattitude.md) is `0` when the X axis is aligned with magnetic north.

The device must have a magnetometer and that sensor must be available. If the magnetometer isn’t currently calibrated, Core Motion prompts the person to move the device to calibrate it.

## See Also

- [static var xArbitraryZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitraryzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitrarycorrectedzvertical.md)
  A reference frame where the Z axis is vertical and has improved rotation accuracy, and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xTrueNorthZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xtruenorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the geographic north pole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xmagneticnorthzvertical)*