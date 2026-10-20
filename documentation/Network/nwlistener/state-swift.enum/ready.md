# NWListener.State.ready

**Framework**: Network  
**Kind**: case  
**Role**: Case

The listener is running and able to receive incoming connections.

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

### States
- [NWListener.State.setup](./setup.md)
  The listener has been initialized but not started.
- [NWListener.State.waiting(_:)](./waiting%28_%29.md)
  The listener is waiting for a network to become available.
- [NWListener.State.failed(_:)](./failed%28_%29.md)
  The listener has encountered a fatal error.
- [NWListener.State.cancelled](./cancelled.md)
  The listener has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/state-swift.enum/ready)*