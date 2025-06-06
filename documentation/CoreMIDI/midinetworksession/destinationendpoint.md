# destinationEndpoint()

**Framework**: Core MIDI  
**Kind**: method

Returns the session’s destination endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func destinationEndpoint() -> MIDIEndpointRef
```

#### Return Value

The destination endpoint.

## See Also

- [var localName: String](midinetworksession/localname.md)
  The name of this session’s entity.
- [var networkName: String](midinetworksession/networkname.md)
  The name with which this session advertises itself over Bonjour.
- [var networkPort: Int](midinetworksession/networkport.md)
  The session’s UDP port.
- [func sourceEndpoint() -> MIDIEndpointRef](midinetworksession/sourceendpoint.md)
  Returns the session’s source endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/destinationendpoint())*