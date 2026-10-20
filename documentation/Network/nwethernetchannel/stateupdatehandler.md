# stateUpdateHandler

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A handler that delivers channel state updates.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@preconcurrency
final var stateUpdateHandler: (@Sendable (NWEthernetChannel.State) -> Void)? { get set }
```

## See Also

### Handling State Updates
- [var state: NWEthernetChannel.State](./state-swift.property.md)
  The current state of the channel.
- [NWEthernetChannel.State](./state-swift.enum.md)
  States indicating whether an Ethernet channel is able to send and receive frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/stateupdatehandler)*