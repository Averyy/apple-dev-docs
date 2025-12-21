# resume(at:)

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
func resume(at time: AVAudioTime?)
```

#### Discussion

Resume the sound event at a specific time

A nil time parameter will resume immediately. The device time is not scaled by UnitsPerSecond and is in seconds.

## Parameters

- `time`: The desired start time based on the engine time retrieved from [PHASEEngine lastRenderTime]


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/resume(at:))*