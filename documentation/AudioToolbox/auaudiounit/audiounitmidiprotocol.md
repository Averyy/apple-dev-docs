# audioUnitMIDIProtocol

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var audioUnitMIDIProtocol: MIDIProtocolID { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) MIDIProtocolID AudioUnitMIDIProtocol;
```

*macOS*

```objc
@property (atomic, readonly) MIDIProtocolID AudioUnitMIDIProtocol;
```

## See Also

### Instance properties
- [var hostMIDIProtocol: MIDIProtocolID](./hostmidiprotocol.md)
- [var midiOutputEventListBlock: AUMIDIEventListBlock?](./midioutputeventlistblock.md)
- [var migrateFromPlugin: [Any]](./migratefromplugin.md)
- [var scheduleMIDIEventListBlock: AUMIDIEventListBlock?](./schedulemidieventlistblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/audiounitmidiprotocol)*