# state

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The current state of the connection.

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
final var state: NWConnection.State { get }
```

## See Also

### Handling State Updates
- [NWConnection.State](./state-swift.enum.md)
  States indicating whether a connection can be used to send and receive data.
- [var stateUpdateHandler: ((NWConnection.State) -> Void)?](./stateupdatehandler.md)
  A handler that receives connection state updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/state-swift.property)*