# isEnabled

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the session is enabled.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

The default value is [`false`](../../Swift/false.md). Disabled sessions don’t appear on the network and can’t initiate or receive connections.

## See Also

### Configuring a Session
- [class func `default`() -> MIDINetworkSession](./default%28%29.md)
  Returns the default singleton session.
- [var connectionPolicy: MIDINetworkConnectionPolicy](./connectionpolicy.md)
  The policy that determines who can connect to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/isenabled)*