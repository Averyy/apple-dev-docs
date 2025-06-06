# start(completion:)

**Framework**: PHASE  
**Kind**: method

Invokes the sound event and runs the specified code on completion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func start() async -> PHASESoundEvent.StartHandlerReason
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func start() async -> PHASESoundEvent.StartHandlerReason
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func start() async -> PHASESoundEvent.StartHandlerReason
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This function returns immediately after instructing the engine to invoke the sound event. If a problem occurs, the function provides an error.

The sound event’s audio plays immediately if the app prepares the sound event in advance. Otherwise, the sound event begins preparing and then plays after preparation completes.

When the sound event plays or errors out, the framework invokes `completionHandler`, passing in a [`PHASESoundEvent.StartHandlerReason`](phasesoundevent/starthandlerreason.md) that explains the reason for the invocation.

> ❗ **Important**:  To play the same sound asset again, create another sound event object. After the first [`start(completion:)`](phasesoundevent/start(completion:).md) call on a particular `PHASESoundEvent` instance, subsequent calls have no effect.

 To play the same sound asset again, create another sound event object. After the first [`start(completion:)`](phasesoundevent/start(completion:).md) call on a particular `PHASESoundEvent` instance, subsequent calls have no effect.

## See Also

- [PHASESoundEvent.StartHandlerReason](phasesoundevent/starthandlerreason.md)
  Indicates the status after starting a sound event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/start(completion:))*