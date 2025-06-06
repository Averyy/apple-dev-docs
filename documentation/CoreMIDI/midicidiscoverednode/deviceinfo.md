# deviceInfo

**Framework**: Core MIDI  
**Kind**: property

The available MIDI-CI device information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var deviceInfo: MIDICIDeviceInfo { get }
```

## See Also

- [var destination: MIDIEntityRef](midicidiscoverednode/destination.md)
  The node’s MIDI destination.
- [var supportsProfiles: Bool](midicidiscoverednode/supportsprofiles.md)
  A Boolean value that indicates whether this node supports MIDI-CI profiles.
- [var supportsProperties: Bool](midicidiscoverednode/supportsproperties.md)
  A Boolean value that indicates whether this node supports MIDI-CI properties.
- [var maximumSysExSize: NSNumber](midicidiscoverednode/maximumsysexsize.md)
  The maximum size of a System Exclusive (SysEx) message this node supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicidiscoverednode/deviceinfo)*