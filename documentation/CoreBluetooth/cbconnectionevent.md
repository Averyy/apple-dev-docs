# CBConnectionEvent

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CBConnectionEvent : NSInteger;
```

## Topics

### Events
- [CBConnectionEvent.peerConnected](./cbconnectionevent/peerconnected.md)
  The peer has connected to the local device.
- [CBConnectionEvent.peerDisconnected](./cbconnectionevent/peerdisconnected.md)
  The peer has disconnected from the local device.
### Initializers
- [init?(rawValue: Int)](./cbconnectionevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Receiving Connection Events
- [func registerForConnectionEvents(options: [CBConnectionEventMatchingOption : Any]?)](./cbcentralmanager/registerforconnectionevents%28options%29.md)
  Register for an event notification when the central manager makes a connection matching the given options.
- [Peripheral Connection Options](./peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [struct CBConnectionEventMatchingOption](./cbconnectioneventmatchingoption.md)
  A set of options to use when registering for connection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectionevent)*