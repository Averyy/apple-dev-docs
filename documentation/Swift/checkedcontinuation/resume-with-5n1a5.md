# resume(with:)

**Framework**: Swift  
**Kind**: method

Resume the task awaiting the continuation by having it either return normally or throw an error based on the state of the given `Result` value.

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
func resume<Er>(with result: sending Result<T, Er>) where E == any Error, Er : Error
```

#### Discussion

A continuation must be resumed exactly once. If the continuation has already been resumed through this object, then the attempt to resume the continuation will trap.

After `resume` enqueues the task, control immediately returns to the caller. The task continues executing when its executor is able to reschedule it.

## Parameters

- `result`: A value to either return or throw from the   continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/checkedcontinuation/resume(with:)-5n1a5)*