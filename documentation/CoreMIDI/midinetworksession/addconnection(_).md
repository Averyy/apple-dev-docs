# addConnection(_:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) addConnection:(MIDINetworkConnection *) connection;
```

## Return Value

[`true`](../../Swift/true.md) if the session successfully added the connection, otherwise [`false`](../../Swift/false.md).

## Parameters

- `connection`: The connection to add.

## See Also

### Managing Connections
- [func connections() -> Set<MIDINetworkConnection>](./connections%28%29.md)
  Returns the session’s set of MIDI network connections.
- [func removeConnection(MIDINetworkConnection) -> Bool](./removeconnection%28_%29.md)
  Removes a connection from this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/addconnection(_:))*