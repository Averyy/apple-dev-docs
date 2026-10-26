# init(hostTime:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio time object with the specified host time.

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
init(hostTime: UInt64)
```

```objc
- (instancetype) initWithHostTime:(uint64_t) hostTime;
```

#### Return Value

A new [`AVAudioTime`](../avaudiotime.md) instance.

## Parameters

- `hostTime`: The host time.

## See Also

### Creating an audio time instance
- [init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)](./init%28audiotimestamp,samplerate%29.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate: Double)](./init%28hosttime,sampletime,atrate%29.md)
  Creates an audio time object with the specified host time, sample time, and sample rate.
- [init(sampleTime: AVAudioFramePosition, atRate: Double)](./init%28sampletime,atrate%29.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [func extrapolateTime(fromAnchor: AVAudioTime) -> AVAudioTime?](./extrapolatetime%28fromanchor%29.md)
  Creates an audio time object by converting between host time and sample time.
- [+ timeWithAudioTimeStamp:sampleRate:](./timewithaudiotimestamp_samplerate_.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [+ timeWithHostTime:sampleTime:atRate:](./timewithhosttime_sampletime_atrate_.md)
  Creates an audio time object with the specified host time, sample time, and sample rate.
- [+ timeWithSampleTime:atRate:](./timewithsampletime_atrate_.md)
  Creates an audio time object with the specified sample time and sample rate.
- [+ timeWithHostTime:](./timewithhosttime_.md)
  Creates an audio time object with the specified host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/init(hosttime:))*