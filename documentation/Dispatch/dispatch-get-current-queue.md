# dispatch_get_current_queue()

**Framework**: Dispatch  
**Kind**: func

Returns the queue on which the currently executing block is running.

**Availability**:
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func dispatch_get_current_queue() -> dispatch_queue_t
```

#### Return Value

Returns the current queue.

#### Discussion

This function is defined to never return `NULL`.

When called from outside of the context of a submitted block, this function returns the main queue if the call is executed from the main thread. If the call is made from any other thread, this function returns the default concurrent queue.

## See Also

- [func dispatch_debugv(dispatch_object_t, UnsafePointer<CChar>, CVaListPointer)](dispatch_debugv(_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_get_current_queue())*