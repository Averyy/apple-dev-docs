# start(at:completion:)

**Framework**: PHASE  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func start(at when: AVAudioTime?) async -> PHASESoundEvent.StartHandlerReason
```

#### Discussion

This function notifies the engine to start the sound event, then returns immediately. Once the sound event is playing (or has failed to start), you will receive a callback via the completion. Playback will begin at the requested time if the sound event has finished preparing in time. You may wait for preparation to finish with the [PHASESoundEvent prepare:completion] method before calling startAtTime, to ensure that the sound event will start at the desired time. However if the desired time is far enough into the future to allow for preparation to happen, you may skip calling prepare entirely and just call startAtTime.

## Parameters

- `when`: The desired start time based on the engine time retrieved from [PHASEEngine lastRenderTime]   If the sound event starts immediately with an audible sound, it will begin rendering at this time.  The sound event will otherwise begin operating at this time.   A nil value will start the sound event immediately   This time is not scaled by unitsPerSecond.
- `handler`: The block that will be called when the sound event has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/start(at:completion:))*