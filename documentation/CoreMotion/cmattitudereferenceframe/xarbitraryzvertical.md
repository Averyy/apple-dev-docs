# xArbitraryZVertical

**Framework**: Core Motion  
**Kind**: property  
**Role**: Type Property

A reference frame where the Z axis is vertical and the X axis points in an arbitrary direction in the horizontal plane.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var xArbitraryZVertical: CMAttitudeReferenceFrame { get }
```

```c
CMAttitudeReferenceFrameXArbitraryZVertical
```

## Mentions

- [Getting processed device-motion data](../getting-processed-device-motion-data.md)

## Discussion

When you start the device-motion service, Core Motion sets the frame of reference to the device’s initial orientation. You might use this option when you don’t need to know the device’s attitude relative to true or magnetic north, and only track rotational changes over time.

This option uses fewer sensors to determine the device attitude, and is more power efficient than the [`xArbitraryCorrectedZVertical`](./xarbitrarycorrectedzvertical.md) option.

> 💡 **Tip**:  Save the first reported attitude value, and compare it to new values to determine changes since the start of the service.

## See Also

### Getting the reference frames
- [static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame](./xarbitrarycorrectedzvertical.md)
  A reference frame where the Z axis is vertical and has improved rotation accuracy, and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xMagneticNorthZVertical: CMAttitudeReferenceFrame](./xmagneticnorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the magnetic north pole.
- [static var xTrueNorthZVertical: CMAttitudeReferenceFrame](./xtruenorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the geographic north pole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe/xarbitraryzvertical)*