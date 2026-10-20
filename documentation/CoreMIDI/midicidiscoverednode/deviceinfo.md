# deviceInfo

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The available MIDI-CI device information.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var deviceInfo: MIDICIDeviceInfo { get }
```

```objc
@property (nonatomic, readonly) MIDICIDeviceInfo * deviceInfo;
```

## See Also

### Inspecting a Node
- [var destination: MIDIEntityRef](./destination.md)
  The node’s MIDI destination.
- [var supportsProfiles: Bool](./supportsprofiles.md)
  A Boolean value that indicates whether this node supports MIDI-CI profiles.
- [var supportsProperties: Bool](./supportsproperties.md)
  A Boolean value that indicates whether this node supports MIDI-CI properties.
- [var maximumSysExSize: NSNumber](./maximumsysexsize.md)
  The maximum size of a System Exclusive (SysEx) message this node supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverednode/deviceinfo)*