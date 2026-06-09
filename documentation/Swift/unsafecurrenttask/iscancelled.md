# isCancelled

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the current task was canceled.

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
var isCancelled: Bool { get }
```

#### Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

This property returns the actual cancellation state of the task, regardless of whether a cancellation shield is active. Use `Task/isCancelled` (the static property) if you need cancellation checking that respects active shields.

##### Instance Property Iscancelled Ignores Task Cancellation Shields

The instance property `task.isCancelled` is not contextual and therefore does not respect cancellation shields. If a task was cancelled and is executing with an active cancellation shield, this property will return the *actual* cancellation status of the specific task.

It is possible to determine if a shield is active and then actively determine that the cancelled status should be temporarily ignored by using this pair of APIs:

```swift
withUnsafeCurrentTask { unsafeTask in
  if unsafeTask.hasActiveCancellationShield {
    false
  } else {
    unsafeTask.isCancelled
  }
}
```

Which is equivalent to the contextually aware static `Task.isCancelled` property:

```swift
// Contextually aware, and equivalent to the snippet using UnsafeCurrentTask:
Task.isCancelled
```

Prefer using `Task.isCancelled` (the static property) in most situations when checking the cancellation status from inside the task.

> **Note**: `Task/isCancelled`

> **Note**: [`checkCancellation()`](task/checkcancellation().md)

> **Note**: [`hasActiveCancellationShield`](task/hasactivecancellationshield.md)

> **Note**: `withTaskCancellationShield(operation:)`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecurrenttask/iscancelled)*