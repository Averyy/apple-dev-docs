# prepare(completion:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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
func prepare(completion handler: (@Sendable (PHASESoundEvent.PrepareHandlerReason) -> Void)? = nil)
```

```swift
func prepare() async -> PHASESoundEvent.PrepareHandlerReason
```

```objc
- (void) prepareWithCompletion:(void (^)(PHASESoundEventPrepareHandlerReason reason)) handler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func prepare() async -> PHASESoundEvent.PrepareHandlerReason
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This function instructs the engine to prepare a sound event and returns immediately. When the preparation completes or fails, the framework runs `completionHandler`.

If you call [`start(completion:)`](./start%28completion%29.md) before `completionHandler` runs, the framework queues the sound event to occur when preparation completes.

## Parameters

- `handler`: Code the framework runs when sound event preparation completes. If you pass `nil`, no code runs when preparation completes.

## See Also

### Preparing Playback
- [PHASESoundEvent.PrepareHandlerReason](./preparehandlerreason.md)
  Indicates the results of sound-event preparation.
- [var prepareState: PHASESoundEvent.PrepareState](./preparestate-swift.property.md)
  The status of sound-event preparation.
- [PHASESoundEvent.PrepareState](./preparestate-swift.enum.md)
  Indicates the state of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/prepare(completion:))*