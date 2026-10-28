# dispatch_debug

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Programmatically logs debug information about a dispatch object.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0
- iPadOS 4.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.9
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```c
extern void dispatch_debug(dispatch_object_t object, const char *message, ...);
```

## Discussion

Debug information is logged to the Console log.  This information can be useful as a debugging tool to view the internal state (current reference count, suspension count, etc.) of a dispatch object at the time the [`dispatch_debug`](./dispatch_debug.md) function is called.

## Parameters

- `object`: The object to introspect.
- `message`: The message to log above and beyond the introspection, in the form of a printf-style format string. The content of this message is appended to the log message separated by a colon, like this: “{*dispatch_object_information*}: *message*”.

## See Also

### Functions
- [func dispatch_get_current_queue() -> dispatch_queue_t](./dispatch_get_current_queue%28%29.md)
  Returns the queue on which the currently executing block is running.
- [func dispatch_debugv(dispatch_object_t, UnsafePointer<CChar>, CVaListPointer)](./dispatch_debugv%28_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_debug)*