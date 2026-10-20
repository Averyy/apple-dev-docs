# NWConnection.State.preparing

**Framework**: Network  
**Kind**: case  
**Role**: Case

The connection in the process of being established.

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
case preparing
```

## See Also

### States
- [NWConnection.State.setup](./setup.md)
  The connection has been initialized but not started.
- [NWConnection.State.waiting(_:)](./waiting%28_%29.md)
  The connection is waiting for a network path change.
- [NWConnection.State.ready](./ready.md)
  The connection is established, and ready to send and receive data.
- [NWConnection.State.failed(_:)](./failed%28_%29.md)
  The connection has disconnected or encountered an error.
- [NWConnection.State.cancelled](./cancelled.md)
  The connection has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/state-swift.enum/preparing)*