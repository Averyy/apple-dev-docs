# MIDIUMPEndpoint

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
class MIDIUMPEndpoint
```

```objc
@interface MIDIUMPEndpoint : NSObject
```

## Topics

### Instance Properties
- [var deviceInfo: MIDI2DeviceInfo](./midiumpendpoint/deviceinfo.md)
- [var endpointType: MIDIUMPCIObjectBackingType](./midiumpendpoint/endpointtype.md)
- [var functionBlocks: [MIDIUMPFunctionBlock]](./midiumpendpoint/functionblocks.md)
- [var hasJRTSReceiveCapability: Bool](./midiumpendpoint/hasjrtsreceivecapability.md)
- [var hasJRTSTransmitCapability: Bool](./midiumpendpoint/hasjrtstransmitcapability.md)
- [var hasStaticFunctionBlocks: Bool](./midiumpendpoint/hasstaticfunctionblocks.md)
- [var midiDestination: MIDIEndpointRef](./midiumpendpoint/mididestination.md)
- [var midiProtocol: MIDIProtocolID](./midiumpendpoint/midiprotocol.md)
- [var midiSource: MIDIEndpointRef](./midiumpendpoint/midisource.md)
- [var name: String](./midiumpendpoint/name.md)
- [var productInstanceID: String](./midiumpendpoint/productinstanceid.md)
- [var supportedMIDIProtocols: MIDIUMPProtocolOptions](./midiumpendpoint/supportedmidiprotocols.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MIDIUMPMutableEndpoint](./midiumpmutableendpoint.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpendpoint)*