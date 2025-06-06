# init(hostTime:sampleTime:atRate:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio time object with the specified host time, sample time, and sample rate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate sampleRate: Double)
```

#### Return Value

A new [`AVAudioTime`](avaudiotime.md) instance.

## Parameters

- `hostTime`: The host time.
- `sampleTime`: The sample time.
- `sampleRate`: The sample rate.

## See Also

- [init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)](avaudiotime/init(audiotimestamp:samplerate:).md)
  Creates an audio time object with the specified timestamp and sample rate.
- [init(hostTime: UInt64)](avaudiotime/init(hosttime:).md)
  Creates an audio time object with the specified host time.
- [init(sampleTime: AVAudioFramePosition, atRate: Double)](avaudiotime/init(sampletime:atrate:).md)
  Creates an audio time object with the specified timestamp and sample rate.
- [func extrapolateTime(fromAnchor: AVAudioTime) -> AVAudioTime?](avaudiotime/extrapolatetime(fromanchor:).md)
  Creates an audio time object by converting between host time and sample time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/init(hosttime:sampletime:atrate:))*