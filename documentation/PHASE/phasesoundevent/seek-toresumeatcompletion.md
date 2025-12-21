# seek(to:resumeAt:completion:)

**Framework**: PHASE  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func seek(to time: Double, resumeAt engineTime: AVAudioTime) async -> PHASESoundEvent.SeekHandlerReason
```

#### Discussion

Seeks all leaf nodes in a PHASESoundEvent to the specified time, and automatically resumes playback at the specified engine time.

This is a low latency convenience method that allows for tight deadlines to be met.  However if the seek fails the node state will not be changed.  You should check the callback and handle the failure appropriately. The time parameter will seek the nodes to the equivalent sample position based on the sample rate of the asset. The engineTime parameter is the engine timestamp to resume rendering at, based off of [PHASEEngine lastRenderTime]. If any leaf nodes do not support seeking, those nodes will ignore this command. Nodes that have finished playing or have stopped will not seek. The time parameter is in seconds and will be scaled by unitsPerSecond. The time in the AVAudioTime structure is not scaled by unitsPerSecond. The engineTime parameter will use the sample time if valid, if not, then the host time if valid.

## Parameters

- `time`: The desired time position in seconds to seek the nodes to.
- `engineTime`: The engine time to resume playback.
- `handler`: The completion callback that will be called when seeking is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/seek(to:resumeat:completion:))*