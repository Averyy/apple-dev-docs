# NWProtocolFramer.Instance.WakeupTime

**Framework**: Network  
**Kind**: enum

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
- [NWProtocolFramer.Instance.WakeupTime.milliseconds(_:)](nwprotocolframer/instance/wakeuptime/milliseconds(_:).md)
  A specific number of milliseconds from now.
- [NWProtocolFramer.Instance.WakeupTime.forever](nwprotocolframer/instance/wakeuptime/forever.md)
  A sentinel value to indicate that no wakeup should be delivered.

## See Also

- [func async(execute: () -> Void)](nwprotocolframer/instance/async(execute:).md)
  Requests that a block be executed on the connection’s internal scheduling context.
- [func scheduleWakeup(wakeupTime: NWProtocolFramer.Instance.WakeupTime)](nwprotocolframer/instance/schedulewakeup(wakeuptime:).md)
  Requests that [`wakeup(framer:)`](nwprotocolframerimplementation/wakeup(framer:).md) be called on your protocol at a specific time in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/wakeuptime)*