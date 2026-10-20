# HMCameraSnapshot

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMCameraSnapshot : HMCameraSource
```

## Topics

### Accessing snapshot properties
- [var captureDate: Date](./hmcamerasnapshot/capturedate.md)
  Date and time at which the snapshot was requested.
### Initializers
- [init()](./hmcamerasnapshot/init%28%29.md)

## Relationships

### Inherits From
- [HMCameraSource](./hmcamerasource.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Taking snapshots
- [func takeSnapshot()](./hmcamerasnapshotcontrol/takesnapshot%28%29.md)
  Takes an image snapshot.
- [var mostRecentSnapshot: HMCameraSnapshot?](./hmcamerasnapshotcontrol/mostrecentsnapshot.md)
  The camera’s most recent snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshot)*