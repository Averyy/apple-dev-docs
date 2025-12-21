# notify(_:atValue:block:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules a notification handler to be called after the shareable event’s signal value equals or exceeds a given value.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func notify(_ listener: MTLSharedEventListener, atValue value: UInt64, block: @escaping MTLSharedEventNotificationBlock)
```

## Mentions

- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md)

## Parameters

- `listener`: The listener object used to dispatch the notification.
- `value`: The minimum value that needs to be signaled before the notification handler is called.
- `block`: The notification handler to call.

## See Also

- [var signaledValue: UInt64](mtlsharedevent/signaledvalue.md)
  The current signal value for the shareable event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedevent/notify(_:atvalue:block:))*