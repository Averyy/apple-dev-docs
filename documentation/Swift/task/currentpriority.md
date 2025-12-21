# currentPriority

**Framework**: Swift  
**Kind**: property

The current task’s priority.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var currentPriority: TaskPriority { get }
```

#### Discussion

If you access this property outside of any task, this queries the system to determine the priority at which the current function is running. If the system can’t provide a priority, this property’s value is `Priority.default`.

## See Also

- [init(name: String?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(name:priority:operation:)-2dll5.md)
  Runs the given nonthrowing operation asynchronously as part of a new  top-level task.
- [init(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(name:priority:operation:)-43wmk.md)
  Runs the given throwing operation asynchronously as part of a new  top-level task.
- [init(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success)](task/init(name:executorpreference:priority:operation:)-59bfi.md)
  Runs the given throwing operation asynchronously as part of a new  top-level task.
- [init(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](task/init(name:executorpreference:priority:operation:)-81pay.md)
  Runs the given nonthrowing operation asynchronously as part of a new  top-level task.
- [static var basePriority: TaskPriority?](task/basepriority.md)
  The current task’s base priority.
- [func withTaskPriorityEscalationHandler<T, E>(operation: () async throws(E) -> T, onPriorityEscalated: (TaskPriority, TaskPriority) -> Void, isolation: isolated (any Actor)?) async throws(E) -> T](withtaskpriorityescalationhandler(operation:onpriorityescalated:isolation:).md)
  Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/currentpriority)*