# MIDIUMPMutableEndpoint

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
class MIDIUMPMutableEndpoint
```

## Topics

### Initializers
- [init?(name: String, deviceInfo: MIDI2DeviceInfo, productInstanceID: String, midiProtocol: MIDIProtocolID, destinationCallback: MIDIReceiveBlock)](midiumpmutableendpoint/init(name:deviceinfo:productinstanceid:midiprotocol:destinationcallback:).md)
### Instance Properties
- [var isEnabled: Bool](midiumpmutableendpoint/isenabled.md)
- [var mutableFunctionBlocks: [MIDIUMPMutableFunctionBlock]](midiumpmutableendpoint/mutablefunctionblocks.md)
### Instance Methods
- [func registerFunctionBlocks([MIDIUMPMutableFunctionBlock], markAsStatic: Bool) throws](midiumpmutableendpoint/registerfunctionblocks(_:markasstatic:).md)
- [func setEnabled(Bool) throws](midiumpmutableendpoint/setenabled(_:).md)
- [func setName(String) throws](midiumpmutableendpoint/setname(_:).md)

## Relationships

### Inherits From
- [MIDIUMPEndpoint](midiumpendpoint.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpmutableendpoint)*