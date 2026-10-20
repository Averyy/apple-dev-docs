# default()

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Type Method

Returns the default singleton session.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> MIDINetworkSession
```

```objc
+ (MIDINetworkSession *) defaultSession;
```

#### Return Value

The default session.

## See Also

### Configuring a Session
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the session is enabled.
- [var connectionPolicy: MIDINetworkConnectionPolicy](./connectionpolicy.md)
  The policy that determines who can connect to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/default())*