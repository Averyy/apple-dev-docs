# state

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The current state of the channel.

**Availability**:
- macOS 10.15+

## Declaration

```swift
final var state: NWEthernetChannel.State { get }
```

## See Also

### Handling State Updates
- [NWEthernetChannel.State](./state-swift.enum.md)
  States indicating whether an Ethernet channel is able to send and receive frames.
- [var stateUpdateHandler: ((NWEthernetChannel.State) -> Void)?](./stateupdatehandler.md)
  A handler that delivers channel state updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.property)*