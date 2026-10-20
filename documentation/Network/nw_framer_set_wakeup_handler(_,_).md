# nw_framer_set_wakeup_handler(_:_:)

**Framework**: Network  
**Kind**: func

Sets a handler to receive scheduled wakeup events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func nw_framer_set_wakeup_handler(_ framer: nw_framer_t, _ wakeup_handler: @escaping nw_framer_wakeup_handler_t)
```

## See Also

- [func nw_framer_schedule_wakeup(nw_framer_t, UInt64)](nw_framer_schedule_wakeup(_:_:).md)
  Requests that the [`nw_framer_wakeup_handler_t`](nw_framer_wakeup_handler_t.md) be called on your protocol at a specific time in the future.
- [var NW_FRAMER_WAKEUP_TIME_FOREVER: UInt64](nw_framer_wakeup_time_forever.md)
  A sentinel value that indicates that no wakeup should be delivered.
- [typealias nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md)
  A handler that delivers a scheduled wakeup event.
- [func nw_framer_async(nw_framer_t, nw_framer_block_t)](nw_framer_async(_:_:).md)
  Requests that a block be executed on the connection’s internal scheduling context.
- [typealias nw_framer_block_t](nw_framer_block_t.md)
  A block to be invoked asynchronously on your framer protocol’s scheduling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_set_wakeup_handler(_:_:))*