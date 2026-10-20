# connections()

**Framework**: Core MIDI  
**Kind**: method

Returns the session’s set of MIDI network connections.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func connections() -> Set<MIDINetworkConnection>
```

#### Return Value

The set of connections.

## See Also

- [func addConnection(MIDINetworkConnection) -> Bool](midinetworksession/addconnection(_:).md)
  Adds a new connection to this session.
- [func removeConnection(MIDINetworkConnection) -> Bool](midinetworksession/removeconnection(_:).md)
  Removes a connection from this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/connections())*