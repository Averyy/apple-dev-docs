# MIDIUMPMutableEndpoint

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
class MIDIUMPMutableEndpoint
```

```objc
@interface MIDIUMPMutableEndpoint : MIDIUMPEndpoint
```

## Topics

### Initializers
- [init?(name: String, deviceInfo: MIDI2DeviceInfo, productInstanceID: String, MIDIProtocol: MIDIProtocolID, destinationCallback: MIDIReceiveBlock)](./midiumpmutableendpoint/init%28name,deviceinfo,productinstanceid,midiprotocol,destinationcallback%29-23tn4.md)
- [init?(name: String, deviceInfo: MIDI2DeviceInfo, productInstanceID: String, midiProtocol: MIDIProtocolID, destinationCallback: MIDIReceiveBlock)](./midiumpmutableendpoint/init%28name,deviceinfo,productinstanceid,midiprotocol,destinationcallback%29-1bsgt.md)
### Instance Properties
- [var isEnabled: Bool](./midiumpmutableendpoint/isenabled.md)
- [var mutableFunctionBlocks: [MIDIUMPMutableFunctionBlock]](./midiumpmutableendpoint/mutablefunctionblocks.md)
### Instance Methods
- [func registerFunctionBlocks([MIDIUMPMutableFunctionBlock], markAsStatic: Bool) throws](./midiumpmutableendpoint/registerfunctionblocks%28_,markasstatic%29.md)
- [func setEnabled(Bool) throws](./midiumpmutableendpoint/setenabled%28_%29.md)
- [func setName(String) throws](./midiumpmutableendpoint/setname%28_%29.md)

## Relationships

### Inherits From
- [MIDIUMPEndpoint](./midiumpendpoint.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpmutableendpoint)*