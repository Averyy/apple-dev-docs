# resume(at:)

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
func resume(at time: AVAudioTime?)
```

#### Discussion

A nil time parameter will resume immediately. The device time is not scaled by UnitsPerSecond and is in seconds.

## Parameters

- `time`: The desired start time based on the engine time retrieved from [PHASEEngine lastRenderTime]


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/resume(at:))*