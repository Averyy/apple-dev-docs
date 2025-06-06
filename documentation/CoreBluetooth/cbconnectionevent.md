# CBConnectionEvent

**Framework**: Core Bluetooth  
**Kind**: enum

A change to the connection state of a peer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum CBConnectionEvent
```

## Topics

### Events
- [CBConnectionEvent.peerConnected](cbconnectionevent/peerconnected.md)
  The peer has connected to the local device.
- [CBConnectionEvent.peerDisconnected](cbconnectionevent/peerdisconnected.md)
  The peer has disconnected from the local device.
### Initializers
- [init?(rawValue: Int)](cbconnectionevent/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func registerForConnectionEvents(options: [CBConnectionEventMatchingOption : Any]?)](cbcentralmanager/registerforconnectionevents(options:).md)
  Register for an event notification when the central manager makes a connection matching the given options.
- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [struct CBConnectionEventMatchingOption](cbconnectioneventmatchingoption.md)
  A set of options to use when registering for connection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectionevent)*