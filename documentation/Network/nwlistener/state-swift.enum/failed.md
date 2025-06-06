# NWListener.State.failed(_:)

**Framework**: Network  
**Kind**: case

The listener has encountered a fatal error.

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
case failed(NWError)
```

## See Also

- [NWListener.State.setup](nwlistener/state-swift.enum/setup.md)
  The listener has been initialized but not started.
- [NWListener.State.waiting(_:)](nwlistener/state-swift.enum/waiting(_:).md)
  The listener is waiting for a network to become available.
- [NWListener.State.ready](nwlistener/state-swift.enum/ready.md)
  The listener is running and able to receive incoming connections.
- [NWListener.State.cancelled](nwlistener/state-swift.enum/cancelled.md)
  The listener has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/state-swift.enum/failed(_:))*