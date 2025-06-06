# localName

**Framework**: Core MIDI  
**Kind**: property

The name of this session’s entity.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var localName: String { get }
```

#### Discussion

The session’s endpoints inherit this value.

## See Also

- [var networkName: String](midinetworksession/networkname.md)
  The name with which this session advertises itself over Bonjour.
- [var networkPort: Int](midinetworksession/networkport.md)
  The session’s UDP port.
- [func sourceEndpoint() -> MIDIEndpointRef](midinetworksession/sourceendpoint.md)
  Returns the session’s source endpoint.
- [func destinationEndpoint() -> MIDIEndpointRef](midinetworksession/destinationendpoint.md)
  Returns the session’s destination endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/localname)*