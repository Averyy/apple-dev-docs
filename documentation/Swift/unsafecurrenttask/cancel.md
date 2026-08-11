# cancel()

**Framework**: Swift  
**Kind**: method

Cancel the current task.

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
func cancel()
```

#### Discussion

The task will be immediately cancelled and cancellation will propagate towards any child tasks it has.

##### Interaction with Task Cancellation Shields

Note that cancellation may not be observed if a task is currently executing with an active task cancellation shield. Refer to cancellation shield documentation for detailed semantics.

> **Note**: `withTaskCancellationShield(operation:)-(()->Value)`

> **Note**: [`hasActiveCancellationShield`](task/hasactivecancellationshield.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecurrenttask/cancel())*