# NWConnection.State.ready

**Framework**: Network  
**Kind**: case

The connection is established, and ready to send and receive data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case ready
```

## See Also

- [NWConnection.State.setup](nwconnection/state-swift.enum/setup.md)
  The connection has been initialized but not started.
- [NWConnection.State.waiting(_:)](nwconnection/state-swift.enum/waiting(_:).md)
  The connection is waiting for a network path change.
- [NWConnection.State.preparing](nwconnection/state-swift.enum/preparing.md)
  The connection in the process of being established.
- [NWConnection.State.failed(_:)](nwconnection/state-swift.enum/failed(_:).md)
  The connection has disconnected or encountered an error.
- [NWConnection.State.cancelled](nwconnection/state-swift.enum/cancelled.md)
  The connection has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/state-swift.enum/ready)*