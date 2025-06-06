# state

**Framework**: Network  
**Kind**: property

The current state of the connection group.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
final var state: NWConnectionGroup.State { get }
```

## See Also

- [var stateUpdateHandler: ((NWConnectionGroup.State) -> Void)?](nwconnectiongroup/stateupdatehandler.md)
  A handler that receives connection group state updates.
- [NWConnectionGroup.State](nwconnectiongroup/state-swift.enum.md)
  States that indicate whether you can use a connection group to send and receive messages.
- [func cancel()](nwconnectiongroup/cancel.md)
  Cancels the connection group object and leaves the network group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.property)*