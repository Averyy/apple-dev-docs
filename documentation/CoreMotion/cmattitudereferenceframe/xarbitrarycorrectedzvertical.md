# xArbitraryCorrectedZVertical

**Framework**: Core Motion  
**Kind**: property

A reference frame where the Z axis is vertical and has improved rotation accuracy, and the X axis points in an arbitrary direction in the horizontal plane.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }
```

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Discussion

When you start the device-motion service, Core Motion uses the current device orientation to set the initial frame of reference. You might use this option when you don’t need to know the device’s attitude relative to true or magnetic north, and only track rotational changes over time.

This option uses the magnetometer to improve long-term accuracy for the z axis (yaw) measurements. The device must have a magnetometer and that sensor must be available and calibrated.

This option requires more CPU usage than the [`xArbitraryZVertical`](cmattitudereferenceframe/xarbitraryzvertical.md) option.

> 💡 **Tip**:  Save the first reported attitude value, and compare it to new values to determine changes since the start of the service.

## See Also

- [static var xArbitraryZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitraryzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xMagneticNorthZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xmagneticnorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the magnetic north pole.
- [static var xTrueNorthZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xtruenorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the geographic north pole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitrarycorrectedzvertical)*