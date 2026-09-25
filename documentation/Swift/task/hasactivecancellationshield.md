# hasActiveCancellationShield

**Framework**: Swift  
**Kind**: property

Checks if the current task is executing in a scope with a task cancellation shield activated by the `withTaskCancellationShield(operation:)-(()->Value)` function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var hasActiveCancellationShield: Bool { get }
```

#### Discussion

An active task cancellation shield prevents a task’s ability to observe if it was cancelled, i.e. the [`isCancelled`](task/iscancelled-swift.type.property.md) property will always return `false` when the task is executing with an active shield.

This property is primarily aimed at  debugging and understanding cancellation behavior in complex call hierarchies, and should not be used in regular control flow.

Returns `true` when executing within a task that has an active cancellation shield.

Cancellation shields are not automatically inherited by child tasks; each child task must install its own shield if needed if it, independently, wanted to ignore cancellation during a specific scope.

> **Note**: `withTaskCancellationShield(operation:)-(()->Value)`

> **Note**: [`hasActiveCancellationShield`](unsafecurrenttask/hasactivecancellationshield.md)

## See Also

- [func withTaskCancellationShield<Value, Failure>(operation: () throws(Failure) -> Value) throws(Failure) -> Value](withtaskcancellationshield(operation:)-2lzl8.md)
  Enters a scope in which a task cancellation shield is active.
- [func withTaskCancellationShield<Value, Failure>(operation: nonisolated(nonsending) () async throws(Failure) -> Value) async throws(Failure) -> Value](withtaskcancellationshield(operation:)-8zlgh.md)
  Enters a scope in which a task cancellation shield is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/hasactivecancellationshield)*