# dispatch_get_current_queue()

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the queue on which the currently executing block is running.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 4.0+ - Deprecated in 6.0
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: unsupported interface

## Declaration

```swift
func dispatch_get_current_queue() -> dispatch_queue_t
```

```c
extern dispatch_queue_tdispatch_get_current_queue();
```

#### Return Value

Returns the current queue.

#### Discussion

This function is defined to never return `NULL`.

When called from outside of the context of a submitted block, this function returns the main queue if the call is executed from the main thread. If the call is made from any other thread, this function returns the default concurrent queue.

## See Also

### Functions
- [func dispatch_debugv(dispatch_object_t, UnsafePointer<CChar>, CVaListPointer)](./dispatch_debugv%28_,_,_%29.md)
- [dispatch_debug](./dispatch_debug.md)
  Programmatically logs debug information about a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_get_current_queue())*