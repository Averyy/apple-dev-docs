# async(execute:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Requests that a block be executed on the connection’s internal scheduling context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final func async(execute: @escaping () -> Void)
```

## Discussion

You should call this if you need to call any framer functions but are in another scheduling context.

## See Also

### Handling Asynchronous Events
- [func scheduleWakeup(wakeupTime: NWProtocolFramer.Instance.WakeupTime)](./schedulewakeup%28wakeuptime%29.md)
  Requests that [`wakeup(framer:)`](../../nwprotocolframerimplementation/wakeup%28framer%29.md) be called on your protocol at a specific time in the future.
- [NWProtocolFramer.Instance.WakeupTime](./wakeuptime.md)
  Times at which to schedule a protocol wakeup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/async(execute:))*