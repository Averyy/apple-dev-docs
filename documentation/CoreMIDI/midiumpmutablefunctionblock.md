# MIDIUMPMutableFunctionBlock

**Framework**: Core MIDI  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class MIDIUMPMutableFunctionBlock
```

## Topics

### Initializers
- [init?(name: String, direction: MIDIUMPFunctionBlockDirection, firstGroup: MIDIUMPGroupNumber, totalGroupsSpanned: MIDIUInteger7, maxSysEx8Streams: MIDIUInteger7, midi1Info: MIDIUMPFunctionBlockMIDI1Info, uiHint: MIDIUMPFunctionBlockUIHint, isEnabled: Bool)](midiumpmutablefunctionblock/init(name:direction:firstgroup:totalgroupsspanned:maxsysex8streams:midi1info:uihint:isenabled:).md)
### Instance Properties
- [var umpEndpoint: MIDIUMPMutableEndpoint?](midiumpmutablefunctionblock/umpendpoint.md)
### Instance Methods
- [func reconfigure(firstGroup: MIDIUMPGroupNumber, direction: MIDIUMPFunctionBlockDirection, MIDI1Info: MIDIUMPFunctionBlockMIDI1Info, UIHint: MIDIUMPFunctionBlockUIHint) throws](midiumpmutablefunctionblock/reconfigure(firstgroup:direction:midi1info:uihint:).md)
- [func setEnabled(Bool) throws](midiumpmutablefunctionblock/setenabled(_:).md)
- [func setName(String) throws](midiumpmutablefunctionblock/setname(_:).md)

## Relationships

### Inherits From
- [MIDIUMPFunctionBlock](midiumpfunctionblock.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpmutablefunctionblock)*