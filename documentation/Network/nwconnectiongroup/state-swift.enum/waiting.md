# NWConnectionGroup.State.waiting(_:)

**Framework**: Network  
**Kind**: case

The connection group is waiting for a network path change.

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
case waiting(NWError)
```

## See Also

- [NWConnectionGroup.State.setup](nwconnectiongroup/state-swift.enum/setup.md)
  You have not yet started the connection group.
- [NWConnectionGroup.State.ready](nwconnectiongroup/state-swift.enum/ready.md)
  The connection group is joined, and ready to send and receive data.
- [NWConnectionGroup.State.failed(_:)](nwconnectiongroup/state-swift.enum/failed(_:).md)
  The connection group encountered a fatal error.
- [NWConnectionGroup.State.cancelled](nwconnectiongroup/state-swift.enum/cancelled.md)
  The connection group has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.enum/waiting(_:))*