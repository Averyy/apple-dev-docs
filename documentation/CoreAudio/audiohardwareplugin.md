# AudioHardwarePlugin

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class AudioHardwarePlugin
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwareplugin/init(id:).md)
### Instance Properties
- [var boxes: [AudioHardwareBox]](audiohardwareplugin/boxes.md)
- [var bundleID: String](audiohardwareplugin/bundleid.md)
- [var clocks: [AudioHardwareClock]](audiohardwareplugin/clocks.md)
- [var devices: [AudioHardwareDevice]](audiohardwareplugin/devices.md)
### Instance Methods
- [func box(forUID: String) throws -> AudioHardwareBox?](audiohardwareplugin/box(foruid:).md)
- [func clock(forUID: String) throws -> AudioHardwareClock?](audiohardwareplugin/clock(foruid:).md)
- [func device(forUID: String) throws -> AudioHardwareDevice?](audiohardwareplugin/device(foruid:).md)

## Relationships

### Inherits From
- [AudioHardwareObject](audiohardwareobject.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareplugin)*