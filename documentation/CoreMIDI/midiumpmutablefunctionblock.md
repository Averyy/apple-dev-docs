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
- [init?(name: String, direction: MIDIUMPFunctionBlockDirection, firstGroup: MIDIUMPGroupNumber, totalGroupsSpanned: MIDIUInteger7, maxSysEx8Streams: MIDIUInteger7, MIDI1Info: MIDIUMPFunctionBlockMIDI1Info, UIHint: MIDIUMPFunctionBlockUIHint, isEnabled: Bool)](midiumpmutablefunctionblock/init(name:direction:firstgroup:totalgroupsspanned:maxsysex8streams:midi1info:uihint:isenabled:)-2i27v.md)
- [init?(name: String, direction: MIDIUMPFunctionBlockDirection, firstGroup: MIDIUMPGroupNumber, totalGroupsSpanned: MIDIUInteger7, maxSysEx8Streams: MIDIUInteger7, midi1Info: MIDIUMPFunctionBlockMIDI1Info, uiHint: MIDIUMPFunctionBlockUIHint, isEnabled: Bool)](midiumpmutablefunctionblock/init(name:direction:firstgroup:totalgroupsspanned:maxsysex8streams:midi1info:uihint:isenabled:)-2izkf.md)
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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpmutablefunctionblock)*