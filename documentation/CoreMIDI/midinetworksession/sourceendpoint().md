# sourceEndpoint()

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

Returns the session’s source endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func sourceEndpoint() -> MIDIEndpointRef
```

```objc
- (MIDIEndpointRef) sourceEndpoint;
```

## Return Value

The source endpoint.

## See Also

### Inspecting a Sessions
- [var localName: String](./localname.md)
  The name of this session’s entity.
- [var networkName: String](./networkname.md)
  The name with which this session advertises itself over Bonjour.
- [var networkPort: Int](./networkport.md)
  The session’s UDP port.
- [func destinationEndpoint() -> MIDIEndpointRef](./destinationendpoint%28%29.md)
  Returns the session’s destination endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/sourceendpoint())*