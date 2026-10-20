# NW_FRAMER_WAKEUP_TIME_FOREVER

**Framework**: Network  
**Kind**: var  
**Role**: Global Variable

A sentinel value that indicates that no wakeup should be delivered.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var NW_FRAMER_WAKEUP_TIME_FOREVER: UInt64 { get }
```

```c
#define NW_FRAMER_WAKEUP_TIME_FOREVER
```

## See Also

### Handling Asynchronous Events
- [func nw_framer_schedule_wakeup(nw_framer_t, UInt64)](./nw_framer_schedule_wakeup%28_,_%29.md)
  Requests that the [`nw_framer_wakeup_handler_t`](./nw_framer_wakeup_handler_t.md) be called on your protocol at a specific time in the future.
- [func nw_framer_set_wakeup_handler(nw_framer_t, nw_framer_wakeup_handler_t)](./nw_framer_set_wakeup_handler%28_,_%29.md)
  Sets a handler to receive scheduled wakeup events.
- [typealias nw_framer_wakeup_handler_t](./nw_framer_wakeup_handler_t.md)
  A handler that delivers a scheduled wakeup event.
- [func nw_framer_async(nw_framer_t, nw_framer_block_t)](./nw_framer_async%28_,_%29.md)
  Requests that a block be executed on the connection’s internal scheduling context.
- [typealias nw_framer_block_t](./nw_framer_block_t.md)
  A block to be invoked asynchronously on your framer protocol’s scheduling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_wakeup_time_forever)*