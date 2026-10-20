# maximumSysExSize

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The maximum size of a System Exclusive (SysEx) message this node supports.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var maximumSysExSize: NSNumber { get }
```

```objc
@property (nonatomic, readonly) NSNumber * maximumSysExSize;
```

## See Also

### Inspecting a Node
- [var destination: MIDIEntityRef](./destination.md)
  The node’s MIDI destination.
- [var deviceInfo: MIDICIDeviceInfo](./deviceinfo.md)
  The available MIDI-CI device information.
- [var supportsProfiles: Bool](./supportsprofiles.md)
  A Boolean value that indicates whether this node supports MIDI-CI profiles.
- [var supportsProperties: Bool](./supportsproperties.md)
  A Boolean value that indicates whether this node supports MIDI-CI properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverednode/maximumsysexsize)*