# CMBodyIdentifiable

**Framework**: Core Motion  
**Kind**: protocol

A type that identifies a physical body or view for device-motion calculations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol CMBodyIdentifiable : NSObjectProtocol
```

#### Overview

Adopt this protocol or use a conforming system type to associate motion sensor updates with a specific view or display. When you set [`deviceMotionBody`](cmmotionmanager/devicemotionbody.md) to an object conforming to [`CMBodyIdentifiable`](cmbodyidentifiable.md), Core Motion automatically calculates motion data, such as 3D orientation and rotation rate, relative to that view rather than the device’s physical coordinate system.

In [`UIKit`](https://developer.apple.com/documentation/uikit), [`UIView`](https://developer.apple.com/documentation/uikit/uiview) conforms to this protocol. Passing a view to [`deviceMotionBody`](cmmotionmanager/devicemotionbody.md) lets your app receive motion data that aligns with your user interface during orientation changes, when running in Stage Manager or Split View on iPad or iPhone Duo.

## Topics

### Motion configuration
- [var deviceMotionBody: (any CMBodyIdentifiable)?](cmmotionmanager/devicemotionbody.md)
  A physical body or view that defines the coordinate system for device-motion data.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Getting processed device-motion data](getting-processed-device-motion-data.md)
  Retrieve motion data that the system processed to remove environmental bias, such as the effects of gravity.
- [class CMDeviceMotion](cmdevicemotion.md)
  Encapsulated measurements of the attitude, rotation rate, and acceleration of a device.
- [class CMAttitude](cmattitude.md)
  The device’s orientation relative to a known frame of reference at a point in time.
- [struct CMAttitudeReferenceFrame](cmattitudereferenceframe.md)
  Constants that indicate the frame of reference for attitude-related motion data.
- [class CMHeadphoneMotionManager](cmheadphonemotionmanager.md)
  An object that starts and manages headphone motion services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbodyidentifiable)*