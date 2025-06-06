# stateUpdateHandler

**Framework**: Network  
**Kind**: property

A handler that delivers channel state updates.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@preconcurrency
final var stateUpdateHandler: ((NWEthernetChannel.State) -> Void)? { get set }
```

## See Also

- [var state: NWEthernetChannel.State](nwethernetchannel/state-swift.property.md)
  The current state of the channel.
- [NWEthernetChannel.State](nwethernetchannel/state-swift.enum.md)
  States indicating whether an Ethernet channel is able to send and receive frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/stateupdatehandler)*