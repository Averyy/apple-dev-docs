# seek(to:completion:)

**Framework**: PHASE  
**Kind**: method

Advances the sound event’s playback position to a specific time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func seek(to time: Double) async -> PHASESoundEvent.SeekHandlerReason
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func seek(to time: Double) async -> PHASESoundEvent.SeekHandlerReason
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `time`: The playback position to advance to. The framework scales this value by  .

## See Also

- [PHASESoundEvent.SeekHandlerReason](phasesoundevent/seekhandlerreason.md)
  Indicates the status after a sound event changes its playback position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/seek(to:completion:))*