# init(name:priority:operation:)

**Framework**: Swift  
**Kind**: init

Runs the given nonthrowing operation asynchronously as part of a new top-level task on behalf of the current actor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
init(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Success)
```

#### Discussion

Use this function when creating asynchronous work that operates on behalf of the synchronous function that calls it. Like `Task.detached(priority:operation:)`, this function creates a separate, top-level task. Unlike `Task.detached(priority:operation:)`, the task created by `Task.init(priority:operation:)` inherits the priority and actor context of the caller, so the operation is treated more like an asynchronous extension to the synchronous operation.

You need to keep a reference to the task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a detached task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## Parameters

- `name`: The high-level human-readable name given for this task
- `priority`: The priority of the task.   Pass   to use the priority from  .
- `operation`: The operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/init(name:priority:operation:)-2dll5)*