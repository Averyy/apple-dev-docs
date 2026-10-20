# connectionPolicy

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The policy that determines who can connect to this session.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var connectionPolicy: MIDINetworkConnectionPolicy { get set }
```

```objc
@property (nonatomic) MIDINetworkConnectionPolicy connectionPolicy;
```

## Topics

### Connection Policies
- [enum MIDINetworkConnectionPolicy](../midinetworkconnectionpolicy.md)

## See Also

### Configuring a Session
- [class func `default`() -> MIDINetworkSession](./default%28%29.md)
  Returns the default singleton session.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the session is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/connectionpolicy)*