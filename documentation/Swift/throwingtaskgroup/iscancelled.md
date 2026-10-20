# isCancelled

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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

To cancel a group, call the `ThrowingTaskGroup.cancelAll()` method.

If the task that’s currently running this group is canceled, the group is also implicitly canceled, which is also reflected in this property’s value.

##### Interaction with task cancellation shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)-(()->Value)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> **See Also**: `withTaskCancellationShield(operation:)-(()->Value)`

## See Also

### Canceling Tasks
- [func cancelAll()](./cancelall%28%29.md)
  Cancel all of the remaining tasks in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/iscancelled)*