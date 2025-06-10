# detached(name:priority:operation:)

**Framework**: Swift  
**Kind**: method

Runs the given nonthrowing operation asynchronously as part of a new top-level task.

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
static func detached(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Success) -> Task<Success, Failure>
```

#### Return Value

A reference to the task.

#### Discussion

Don’t use a detached task if it’s possible to model the operation using structured concurrency features like child tasks. Child tasks inherit the parent task’s priority and task-local storage, and canceling a parent task automatically cancels all of its child tasks. You need to handle these considerations manually with a detached task.

You need to keep a reference to the detached task if you want to cancel it by calling the `Task.cancel()` method. Discarding your reference to a detached task doesn’t implicitly cancel that task, it only makes it impossible for you to explicitly cancel the task.

## Parameters

- `name`: Human readable name of the task.
- `priority`: The priority of the task.
- `operation`: The operation to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/detached(name:priority:operation:)-9xki7)*