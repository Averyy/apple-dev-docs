# midiOutputEventListBlock

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
var midiOutputEventListBlock: AUMIDIEventListBlock? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, nullable) AUMIDIEventListBlock MIDIOutputEventListBlock;
```

*macOS*

```objc
@property (atomic, copy, nullable) AUMIDIEventListBlock MIDIOutputEventListBlock;
```

## See Also

### Instance properties
- [var audioUnitMIDIProtocol: MIDIProtocolID](./audiounitmidiprotocol.md)
- [var hostMIDIProtocol: MIDIProtocolID](./hostmidiprotocol.md)
- [var migrateFromPlugin: [Any]](./migratefromplugin.md)
- [var scheduleMIDIEventListBlock: AUMIDIEventListBlock?](./schedulemidieventlistblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/midioutputeventlistblock)*