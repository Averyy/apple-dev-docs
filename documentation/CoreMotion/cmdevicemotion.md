# CMDeviceMotion

**Framework**: Core Motion  
**Kind**: class

Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMDeviceMotion
```

#### Overview

An application receives or samples `CMDeviceMotion` objects at regular intervals after calling the [`startDeviceMotionUpdates(using:to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(using:to:withhandler:).md) method, the [`startDeviceMotionUpdates(to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(to:withhandler:).md) method, the [`startDeviceMotionUpdates(using:)`](cmmotionmanager/startdevicemotionupdates(using:).md) method, or the [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md) method of the [`CMMotionManager`](cmmotionmanager.md) class.

The accelerometer measures the sum of two acceleration vectors: gravity and user acceleration. User acceleration is the acceleration that the user imparts to the device. Because Core Motion is able to track a device’s attitude using both the gyroscope and the accelerometer, it can differentiate between gravity and user acceleration. A `CMDeviceMotion` object provides both measurements in the [`gravity`](cmdevicemotion/gravity.md) and [`userAcceleration`](cmdevicemotion/useracceleration.md) properties.

## Topics

### Getting Attitude and Rotation Rate
- [var attitude: CMAttitude](cmdevicemotion/attitude.md)
  The attitude of the device.
- [var rotationRate: CMRotationRate](cmdevicemotion/rotationrate.md)
  The rotation rate of the device.
### Getting Acceleration Data
- [var gravity: CMAcceleration](cmdevicemotion/gravity.md)
  The gravity acceleration vector expressed in the device’s reference frame.
- [var userAcceleration: CMAcceleration](cmdevicemotion/useracceleration.md)
  The acceleration that the user is giving to the device.
### Getting the Calibrated Magnetic Field
- [var magneticField: CMCalibratedMagneticField](cmdevicemotion/magneticfield.md)
  Returns the magnetic field vector with respect to the device.
- [struct CMCalibratedMagneticField](cmcalibratedmagneticfield.md)
  Calibrated magnetic field data and an estimate of the accuracy of the calibration.
- [enum CMMagneticFieldCalibrationAccuracy](cmmagneticfieldcalibrationaccuracy.md)
  Indicates the calibration accuracy of a magnetic field estimate
### Getting the Heading
- [var heading: Double](cmdevicemotion/heading.md)
  The heading angle (measured in degrees) relative to the current reference frame.
### Getting the Sensor Location
- [var sensorLocation: CMDeviceMotion.SensorLocation](cmdevicemotion/sensorlocation-swift.property.md)
  The location of the sensors that compute the device-motion data.
- [CMDeviceMotion.SensorLocation](cmdevicemotion/sensorlocation-swift.enum.md)
  Defines the device’s sensor locations.

## Relationships

### Inherits From
- [CMLogItem](cmlogitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Getting processed device-motion data](getting-processed-device-motion-data.md)
  Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.
- [class CMAttitude](cmattitude.md)
  The device’s orientation relative to a known frame of reference at a point in time.
- [struct CMAttitudeReferenceFrame](cmattitudereferenceframe.md)
  Constants that indicate the frame of reference for attitude-related motion data.
- [class CMHeadphoneMotionManager](cmheadphonemotionmanager.md)
  An object that starts and manages headphone motion services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion)*