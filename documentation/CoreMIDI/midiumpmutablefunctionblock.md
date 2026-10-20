# MIDIUMPMutableFunctionBlock

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

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

```objc
@interface MIDIUMPMutableFunctionBlock : MIDIUMPFunctionBlock
```

## Topics

### Initializers
- [init?(name: String, direction: MIDIUMPFunctionBlockDirection, firstGroup: MIDIUMPGroupNumber, totalGroupsSpanned: MIDIUInteger7, maxSysEx8Streams: MIDIUInteger7, MIDI1Info: MIDIUMPFunctionBlockMIDI1Info, UIHint: MIDIUMPFunctionBlockUIHint, isEnabled: Bool)](./midiumpmutablefunctionblock/init%28name,direction,firstgroup,totalgroupsspanned,maxsysex8streams,midi1info,uihint,isenabled%29-2i27v.md)
- [init?(name: String, direction: MIDIUMPFunctionBlockDirection, firstGroup: MIDIUMPGroupNumber, totalGroupsSpanned: MIDIUInteger7, maxSysEx8Streams: MIDIUInteger7, midi1Info: MIDIUMPFunctionBlockMIDI1Info, uiHint: MIDIUMPFunctionBlockUIHint, isEnabled: Bool)](./midiumpmutablefunctionblock/init%28name,direction,firstgroup,totalgroupsspanned,maxsysex8streams,midi1info,uihint,isenabled%29-2izkf.md)
### Instance Properties
- [var umpEndpoint: MIDIUMPMutableEndpoint?](./midiumpmutablefunctionblock/umpendpoint.md)
### Instance Methods
- [func reconfigure(firstGroup: MIDIUMPGroupNumber, direction: MIDIUMPFunctionBlockDirection, MIDI1Info: MIDIUMPFunctionBlockMIDI1Info, UIHint: MIDIUMPFunctionBlockUIHint) throws](./midiumpmutablefunctionblock/reconfigure%28firstgroup,direction,midi1info,uihint%29.md)
- [func setEnabled(Bool) throws](./midiumpmutablefunctionblock/setenabled%28_%29.md)
- [func setName(String) throws](./midiumpmutablefunctionblock/setname%28_%29.md)

## Relationships

### Inherits From
- [MIDIUMPFunctionBlock](./midiumpfunctionblock.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpmutablefunctionblock)*