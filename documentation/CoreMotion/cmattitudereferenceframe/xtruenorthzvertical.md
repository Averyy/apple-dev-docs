# xTrueNorthZVertical

**Framework**: Core Motion  
**Kind**: property

A reference frame where the Z axis is vertical and the X axis points to the geographic north pole.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var xTrueNorthZVertical: CMAttitudeReferenceFrame { get }
```

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Discussion

Use this option to determine the attitude of the device relative to true north. For example, you might use this to implement more precise navigation. The [`yaw`](cmattitude/yaw.md) (Z-axis) value in [`CMAttitude`](cmattitude.md) is `0` when the X axis is aligned with true north.

The device must have a magnetometer and that sensor must be available. Location services must also be available to calculate the difference between magnetic and true north. If the magnetometer isn’t currently calibrated, Core Motion prompts the person to move the device to calibrate it.

## See Also

- [static var xArbitraryZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitraryzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitrarycorrectedzvertical.md)
  A reference frame where the Z axis is vertical and has improved rotation accuracy, and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xMagneticNorthZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xmagneticnorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the magnetic north pole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xtruenorthzvertical)*