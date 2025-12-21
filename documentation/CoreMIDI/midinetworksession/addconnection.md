# addConnection(_:)

**Framework**: Core MIDI  
**Kind**: method

Adds a new connection to this session.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func addConnection(_ connection: MIDINetworkConnection) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the session successfully added the connection, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `connection`: The connection to add.

## See Also

- [func connections() -> Set<MIDINetworkConnection>](midinetworksession/connections.md)
  Returns the session’s set of MIDI network connections.
- [func removeConnection(MIDINetworkConnection) -> Bool](midinetworksession/removeconnection(_:).md)
  Removes a connection from this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/addconnection(_:))*