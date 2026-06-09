# isCancelled

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the group was canceled.

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

To cancel a group, call the `TaskGroup.cancelAll()` method.

If the task that’s currently running this group is canceled, the group is also implicitly canceled, which is also reflected in this property’s value.

##### Interaction with Task Cancellation Shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> **Note**: `withTaskCancellationShield(operation:)`

## See Also

- [func cancelAll()](taskgroup/cancelall.md)
  Cancel all of the remaining tasks in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/iscancelled)*