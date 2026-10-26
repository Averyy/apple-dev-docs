# dispatch_workloop_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias dispatch_workloop_t = DispatchWorkloop
```

```c
typedef NSObject<OS_dispatch_workloop> * dispatch_workloop_t;
```

## See Also

### Creating a Dispatch Workloop
- [dispatch_workloop_create](./dispatch_workloop_create.md)
  Creates a new workloop with the specified label.
- [dispatch_workloop_create_inactive](./dispatch_workloop_create_inactive.md)
  Creates a new inactive workloop with the specified label.
- [OS_dispatch_workloop](./os_dispatch_workloop.md)
  A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_workloop_t)*