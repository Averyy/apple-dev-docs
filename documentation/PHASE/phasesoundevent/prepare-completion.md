# prepare(completion:)

**Framework**: PHASE  
**Kind**: method

Enables a sound event to play and runs the argument code when the sound event plays back.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func prepare() async -> PHASESoundEvent.PrepareHandlerReason
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func prepare() async -> PHASESoundEvent.PrepareHandlerReason
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func prepare() async -> PHASESoundEvent.PrepareHandlerReason
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This function instructs the engine to prepare a sound event and returns immediately. When the preparation completes or fails, the framework runs `completionHandler`.

If you call [`start(completion:)`](phasesoundevent/start(completion:).md) before `completionHandler` runs, the framework queues the sound event to occur when preparation completes.

## Parameters

- `handler`: Code the framework runs when sound event preparation completes. If you pass  , no code runs when preparation completes.

## See Also

- [PHASESoundEvent.PrepareHandlerReason](phasesoundevent/preparehandlerreason.md)
  Indicates the results of sound-event preparation.
- [var prepareState: PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.property.md)
  The status of sound-event preparation.
- [PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.enum.md)
  Indicates the state of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/prepare(completion:))*