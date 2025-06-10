# CMAttitudeReferenceFrame

**Framework**: Core Motion  
**Kind**: struct

Constants that indicate the frame of reference for attitude-related motion data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMAttitudeReferenceFrame
```

#### Overview

When you start a service that reports the device’s attitude in three-dimensional space, Core Motion establishes a frame of reference for reporting pitch, roll, and yaw values. All subsequent data values specify the device attitude relative to this frame of reference. To get a list of the currently available reference frames for the current device, call the [`availableAttitudeReferenceFrames()`](cmmotionmanager/availableattitudereferenceframes().md) class method.

When starting services, it’s your responsibility to specify a reference frame that’s available on the current device. Services that don’t let you specify a reference frame explicitly rely on the value in the [`attitudeReferenceFrame`](cmmotionmanager/attitudereferenceframe.md) property of [`CMMotionManager`](cmmotionmanager.md).

## Topics

### Getting the reference frames
- [static var xArbitraryZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitraryzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xArbitraryCorrectedZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xarbitrarycorrectedzvertical.md)
  A reference frame where the Z axis is vertical and has improved rotation accuracy, and the X axis points in an arbitrary direction in the horizontal plane.
- [static var xMagneticNorthZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xmagneticnorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the magnetic north pole.
- [static var xTrueNorthZVertical: CMAttitudeReferenceFrame](cmattitudereferenceframe/xtruenorthzvertical.md)
  A reference frame where the Z axis is vertical and the X axis points to the geographic north pole.
### Initializers
- [init(rawValue: UInt)](cmattitudereferenceframe/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Getting processed device-motion data](getting-processed-device-motion-data.md)
  Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.
- [class CMDeviceMotion](cmdevicemotion.md)
  Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- [class CMAttitude](cmattitude.md)
  The device’s orientation relative to a known frame of reference at a point in time.
- [class CMHeadphoneMotionManager](cmheadphonemotionmanager.md)
  An object that starts and manages headphone motion services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)*