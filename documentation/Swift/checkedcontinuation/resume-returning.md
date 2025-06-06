# resume(returning:)

**Framework**: Swift  
**Kind**: method

Resume the task awaiting the continuation by having it return normally from its suspension point.

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
func resume(returning value: sending T)
```

#### Discussion

A continuation must be resumed exactly once. If the continuation has already been resumed through this object, then the attempt to resume the continuation will trap.

After `resume` enqueues the task, control immediately returns to the caller. The task continues executing when its executor is able to reschedule it.

## Parameters

- `value`: The value to return from the continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/checkedcontinuation/resume(returning:))*