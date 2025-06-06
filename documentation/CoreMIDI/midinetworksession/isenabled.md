# isEnabled

**Framework**: Core MIDI  
**Kind**: property

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

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). Disabled sessions don’t appear on the network and can’t initiate or receive connections.

## See Also

- [class func `default`() -> MIDINetworkSession](midinetworksession/default.md)
  Returns the default singleton session.
- [var connectionPolicy: MIDINetworkConnectionPolicy](midinetworksession/connectionpolicy.md)
  The policy that determines who can connect to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/isenabled)*