# connections()

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSSet<MIDINetworkConnection *> *) connections;
```

## Return Value

The set of connections.

## See Also

### Managing Connections
- [func addConnection(MIDINetworkConnection) -> Bool](./addconnection%28_%29.md)
  Adds a new connection to this session.
- [func removeConnection(MIDINetworkConnection) -> Bool](./removeconnection%28_%29.md)
  Removes a connection from this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/connections())*