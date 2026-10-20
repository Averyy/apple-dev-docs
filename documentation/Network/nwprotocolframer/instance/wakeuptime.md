# NWProtocolFramer.Instance.WakeupTime

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

Times at which to schedule a protocol wakeup.

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
enum WakeupTime
```

## Topics

### Time Values
- [NWProtocolFramer.Instance.WakeupTime.milliseconds(_:)](./wakeuptime/milliseconds%28_%29.md)
  A specific number of milliseconds from now.
- [NWProtocolFramer.Instance.WakeupTime.forever](./wakeuptime/forever.md)
  A sentinel value to indicate that no wakeup should be delivered.

## See Also

### Handling Asynchronous Events
- [func async(execute: () -> Void)](./async%28execute%29.md)
  Requests that a block be executed on the connection’s internal scheduling context.
- [func scheduleWakeup(wakeupTime: NWProtocolFramer.Instance.WakeupTime)](./schedulewakeup%28wakeuptime%29.md)
  Requests that [`wakeup(framer:)`](../../nwprotocolframerimplementation/wakeup%28framer%29.md) be called on your protocol at a specific time in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/wakeuptime)*