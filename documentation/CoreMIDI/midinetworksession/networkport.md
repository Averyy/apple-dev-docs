# networkPort

**Framework**: Core MIDI  
**Kind**: property

The session’s UDP port.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var networkPort: Int { get }
```

## See Also

- [var localName: String](midinetworksession/localname.md)
  The name of this session’s entity.
- [var networkName: String](midinetworksession/networkname.md)
  The name with which this session advertises itself over Bonjour.
- [func sourceEndpoint() -> MIDIEndpointRef](midinetworksession/sourceendpoint.md)
  Returns the session’s source endpoint.
- [func destinationEndpoint() -> MIDIEndpointRef](midinetworksession/destinationendpoint.md)
  Returns the session’s destination endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/networkport)*