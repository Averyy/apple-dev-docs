# dispatch_once_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

A predicate for use with the `dispatch_once` function.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef intptr_t dispatch_once_t;
```

## Discussion

Variables of this type must have global or static scope.  The result of using this type with automatic or dynamic allocation is undefined. See [`dispatch_get_global_queue`](./dispatch_get_global_queue.md) for details.

## See Also

### Executing a Task Only Once
- [dispatch_once](./dispatch_once-c.func.md)
  Executes a block object only once for the lifetime of an application.
- [dispatch_once_f](./dispatch_once_f-c.func.md)
  Executes an application-defined function only once for the lifetime of an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_once_t)*