# dispatch_debugv(_:_:_:)

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

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
func dispatch_debugv(_ object: dispatch_object_t, _ message: UnsafePointer<CChar>, _ ap: CVaListPointer)
```

```c
extern void dispatch_debugv(dispatch_object_t object, const char *message, va_list ap);
```

## See Also

### Functions
- [func dispatch_get_current_queue() -> dispatch_queue_t](./dispatch_get_current_queue%28%29.md)
  Returns the queue on which the currently executing block is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_debugv(_:_:_:))*