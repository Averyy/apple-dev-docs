# stateUpdateHandler

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A handler that receives connection state updates.

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
@preconcurrency
final var stateUpdateHandler: (@Sendable (NWConnection.State) -> Void)? { get set }
```

## See Also

### Handling State Updates
- [var state: NWConnection.State](./state-swift.property.md)
  The current state of the connection.
- [NWConnection.State](./state-swift.enum.md)
  States indicating whether a connection can be used to send and receive data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/stateupdatehandler)*