# hasActiveCancellationShield

**Framework**: Swift  
**Kind**: property

Checks if the current task is executing in a scope with a task cancellation shield activated by the `withTaskCancellationShield(operation:)` function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var hasActiveCancellationShield: Bool { get }
```

#### Discussion

An active task cancellation shield prevents a task’s ability to observe if it was cancelled, i.e. the `Task/isCancelled` property will always return `false` when the task is executing with an active shield.

This property is primarily aimed at  debugging and understanding cancellation behavior in complex call hierarchies, and should not be used in regular control flow.

Returns `true` when executing within a task that has an active cancellation shield.

Cancellation shields are not automatically inherited by child tasks; each child task must install its own shield if needed if it, independently, wanted to ignore cancellation during a specific scope.

> **Note**: `withTaskCancellationShield(operation:)`

> **Note**: [`hasActiveCancellationShield`](unsafecurrenttask/hasactivecancellationshield.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/hasactivecancellationshield)*