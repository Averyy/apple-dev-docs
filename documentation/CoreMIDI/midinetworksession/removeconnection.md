# removeConnection(_:)

**Framework**: Core MIDI  
**Kind**: method

Removes a connection from this session.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func removeConnection(_ connection: MIDINetworkConnection) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the session successfully removed the connection, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `connection`: The connection to remove.

## See Also

- [func connections() -> Set<MIDINetworkConnection>](midinetworksession/connections.md)
  Returns the session’s set of MIDI network connections.
- [func addConnection(MIDINetworkConnection) -> Bool](midinetworksession/addconnection(_:).md)
  Adds a new connection to this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/removeconnection(_:))*