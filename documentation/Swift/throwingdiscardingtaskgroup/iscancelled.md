# isCancelled

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the group was canceled.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

#### Discussion

To cancel a group, call the `ThrowingDiscardingTaskGroup.cancelAll()` method.

If the task that’s currently running this group is canceled, the group is also implicitly canceled, which is also reflected in this property’s value.

##### Interaction with Task Cancellation Shields

Cancellation may be suppressed by an active task cancellation shield (`withTaskCancellationShield(operation:)`), which may cause `isCancelled` to return `false` even though the task has been cancelled externally.

> **Note**: `withTaskCancellationShield(operation:)`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/iscancelled)*