# currentPriority

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

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

Available when `Success` is `Never` and `Failure` is `Never`.

#### Discussion

If you access this property outside of any task, this queries the system to determine the priority at which the current function is running. If the system can’t provide a priority, this property’s value is `Priority.default`.

## See Also

### Creating a Task
- [init(name: String?, priority: TaskPriority?, operation: sending () async -> Success)](./init%28name,priority,operation%29-2dll5.md)
  Runs the given nonthrowing operation asynchronously as part of a new *unstructured* top-level task.
- [init(name: String?, priority: TaskPriority?, operation: sending () async throws -> Success)](./init%28name,priority,operation%29-43wmk.md)
  Runs the given throwing operation asynchronously as part of a new *unstructured* top-level task.
- [init(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async throws -> Success)](./init%28name,executorpreference,priority,operation%29-59bfi.md)
  Runs the given throwing operation asynchronously as part of a new *unstructured* top-level task.
- [init(name: String?, executorPreference: (any TaskExecutor)?, priority: TaskPriority?, operation: sending () async -> Success)](./init%28name,executorpreference,priority,operation%29-81pay.md)
  Runs the given nonthrowing operation asynchronously as part of a new *unstructured* top-level task.
- [static var basePriority: TaskPriority?](./basepriority.md)
  The current task’s base priority.
- [func withTaskPriorityEscalationHandler<T, E>(operation: nonisolated(nonsending) () async throws(E) -> T, onPriorityEscalated: (TaskPriority, TaskPriority) -> Void) async throws(E) -> T](../withtaskpriorityescalationhandler%28operation,onpriorityescalated%29.md)
  Runs the passed `operation` while registering a task priority escalation handler. The handler will be triggered concurrently to the current task if the current is subject to priority escalation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/currentpriority)*