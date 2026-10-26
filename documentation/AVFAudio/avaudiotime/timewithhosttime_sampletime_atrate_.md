# timeWithHostTime:sampleTime:atRate:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (instancetype) timeWithHostTime:(uint64_t) hostTime sampleTime:(AVAudioFramePosition) sampleTime atRate:(double) sampleRate;
```

#### Return Value

A new [`AVAudioTime`](../avaudiotime.md) instance.

## Parameters

- `hostTime`: The host time.
- `sampleTime`: The sample time.
- `sampleRate`: The sample rate.

## See Also

### Creating an audio time instance
- [init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)](./init%28audiotimestamp,samplerate%29.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [init(hostTime: UInt64)](./init%28hosttime%29.md)
  Creates an audio time object with the specified host time.
- [init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate: Double)](./init%28hosttime,sampletime,atrate%29.md)
  Creates an audio time object with the specified host time, sample time, and sample rate.
- [init(sampleTime: AVAudioFramePosition, atRate: Double)](./init%28sampletime,atrate%29.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [+ timeWithAudioTimeStamp:sampleRate:](./timewithaudiotimestamp_samplerate_.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [+ timeWithSampleTime:atRate:](./timewithsampletime_atrate_.md)
  Creates an audio time object with the specified sample time and sample rate.
- [+ timeWithHostTime:](./timewithhosttime_.md)
  Creates an audio time object with the specified host time.
- [func extrapolateTime(fromAnchor: AVAudioTime) -> AVAudioTime?](./extrapolatetime%28fromanchor%29.md)
  Creates an audio time object by converting between host time and sample time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/timewithhosttime:sampletime:atrate:)*