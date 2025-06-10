# CMAttitude

**Framework**: Core Motion  
**Kind**: class

The device’s orientation relative to a known frame of reference at a point in time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMAttitude
```

#### Overview

The `CMAttitude` class offers three different mathematical representations of attitude: a rotation matrix, a quaternion, and Euler angles (roll, pitch, and yaw values). You access `CMAttitude` objects through the attitude property of each [`CMDeviceMotion`](cmdevicemotion.md) objects passed to an application. An application starts receiving these device-motion objects as a result of calling the [`startDeviceMotionUpdates(using:to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(using:to:withhandler:).md) method, the [`startDeviceMotionUpdates(to:withHandler:)`](cmmotionmanager/startdevicemotionupdates(to:withhandler:).md) method, the [`startDeviceMotionUpdates(using:)`](cmmotionmanager/startdevicemotionupdates(using:).md) method, or the [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md) method of the [`CMMotionManager`](cmmotionmanager.md) class.

> **Note**:  Core Motion outputs a direction cosine matrix (DCM)—basically a rotation from the last “old” orientation to the new orientation of the device.

## Topics

### Getting a Mathematical Representation of Attitude as Euler Angles
- [var roll: Double](cmattitude/roll.md)
  The roll of the device, in radians.
- [var pitch: Double](cmattitude/pitch.md)
  The pitch of the device, in radians.
- [var yaw: Double](cmattitude/yaw.md)
  The yaw of the device, in radians.
### Getting a Mathematical Representation of Attitude as a Rotation Matrix
- [var rotationMatrix: CMRotationMatrix](cmattitude/rotationmatrix.md)
  Returns a rotation matrix representing the device’s attitude.
- [struct CMRotationMatrix](cmrotationmatrix.md)
  The type of a structure representing a rotation matrix.
### Getting a Mathematical Representation of Attitude as a Quaternion
- [var quaternion: CMQuaternion](cmattitude/quaternion.md)
  Returns a quaternion representing the device’s attitude.
- [struct CMQuaternion](cmquaternion.md)
  The type for a quaternion representing a measurement of attitude.
### Obtaining the Change in Attitude
- [func multiply(byInverseOf: CMAttitude)](cmattitude/multiply(byinverseof:).md)
  Yields the change in attitude given a specific attitude.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class CMDeviceMotion](cmdevicemotion.md)
  Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- [struct CMAttitudeReferenceFrame](cmattitudereferenceframe.md)
  Constants that indicate the frame of reference for attitude-related motion data.
- [class CMHeadphoneMotionManager](cmheadphonemotionmanager.md)
  An object that starts and manages headphone motion services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitude)*