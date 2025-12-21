# AudioHardwarePlugin

**Framework**: Core Audio  
**Kind**: class

Instances of the AudioHardwarePlugin class encapsulate a single audio HAL plugin, which is a CFBundle loaded by the HAL as a driver to implement device-specific properties and routines.

**Availability**:
- Mac Catalyst ?+
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
  An array of AudioHardwareBoxes that represent all the box objects currently provided by the plugin.
- [var bundleID: String](audiohardwareplugin/bundleid.md)
  A String that contains the bundle identifier for the plugin.
- [var clocks: [AudioHardwareClock]](audiohardwareplugin/clocks.md)
  An array of AudioHardwareClocks that represent all the clock objects currently provided by the plugin.
- [var devices: [AudioHardwareDevice]](audiohardwareplugin/devices.md)
  An array of AudioHardwareDevices that represent all the devices currently provided by the plugin.
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