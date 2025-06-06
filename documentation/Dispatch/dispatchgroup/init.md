# init()

**Framework**: Dispatch  
**Kind**: init

Creates a new group to which you can assign block objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init()
```

#### Return Value

The newly created group. In Objective-C returns `NULL` on failure.

#### Discussion

This function creates a new group with which block objects can be associated (by using the [`dispatch_group_async`](dispatch_group_async.md) function). The dispatch group maintains a count of its outstanding associated tasks, incrementing the count when a new task is associated and decrementing it when a task completes. Functions such as [`dispatch_group_notify`](dispatch_group_notify.md) and [`dispatch_group_wait`](dispatch_group_wait.md) use that count to allow your application to determine when all tasks associated with the group have completed. At that time, your application can take any appropriate action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/init())*