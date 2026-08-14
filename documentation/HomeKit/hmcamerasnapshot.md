# HMCameraSnapshot

**Framework**: HomeKit  
**Kind**: class

An object that represents a snapshot taken from a camera.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraSnapshot
```

## Topics

### Accessing snapshot properties
- [var captureDate: Date](hmcamerasnapshot/capturedate.md)
  Date and time at which the snapshot was requested.
### Initializers
- [init()](hmcamerasnapshot/init.md)

## Relationships

### Inherits From
- [HMCameraSource](hmcamerasource.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func takeSnapshot()](hmcamerasnapshotcontrol/takesnapshot.md)
  Takes an image snapshot.
- [var mostRecentSnapshot: HMCameraSnapshot?](hmcamerasnapshotcontrol/mostrecentsnapshot.md)
  The camera’s most recent snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshot)*