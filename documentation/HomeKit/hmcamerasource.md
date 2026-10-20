# HMCameraSource

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

An abstract class for a camera’s data source.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraSource
```

```objc
@interface HMCameraSource : NSObject
```

## Topics

### Getting the properties
- [var aspectRatio: Double](./hmcamerasource/aspectratio.md)
  The aspect ratio of the camera.
### Initializers
- [init()](./hmcamerasource/init%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HMCameraSnapshot](./hmcamerasnapshot.md)
- [HMCameraStream](./hmcamerastream.md)
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

### Creating a camera view
- [init(source: HMCameraSource)](./cameraview/init%28source%29.md)
  Creates a new camera view using the given source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasource)*