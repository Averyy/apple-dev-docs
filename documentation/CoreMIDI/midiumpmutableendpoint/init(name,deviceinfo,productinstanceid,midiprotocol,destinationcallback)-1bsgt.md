# init(name:deviceInfo:productInstanceID:midiProtocol:destinationCallback:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init?(name: String, deviceInfo: MIDI2DeviceInfo, productInstanceID: String, midiProtocol MIDIProtocol: MIDIProtocolID, destinationCallback: @escaping MIDIReceiveBlock)
```

```objc
- (instancetype) initWithName:(NSString *) name deviceInfo:(MIDI2DeviceInfo *) deviceInfo productInstanceID:(NSString *) productInstanceID MIDIProtocol:(MIDIProtocolID) MIDIProtocol destinationCallback:(MIDIReceiveBlock) destinationCallback;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiumpmutableendpoint/init(name:deviceinfo:productinstanceid:midiprotocol:destinationcallback:)-1bsgt)*