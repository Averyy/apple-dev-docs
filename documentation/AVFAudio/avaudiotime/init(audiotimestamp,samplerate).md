# init(audioTimeStamp:sampleRate:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio time object with the specified timestamp and sample rate.

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
init(audioTimeStamp ts: UnsafePointer<AudioTimeStamp>, sampleRate: Double)
```

```objc
- (instancetype) initWithAudioTimeStamp:(const AudioTimeStamp *) ts sampleRate:(double) sampleRate;
```

#### Return Value

A new [`AVAudioTime`](../avaudiotime.md) instance.

## Parameters

- `ts`: The timestamp.
- `sampleRate`: The sample rate.

## See Also

### Creating an audio time instance
- [init(hostTime: UInt64)](./init%28hosttime%29.md)
  Creates an audio time object with the specified host time.
- [init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate: Double)](./init%28hosttime,sampletime,atrate%29.md)
  Creates an audio time object with the specified host time, sample time, and sample rate.
- [init(sampleTime: AVAudioFramePosition, atRate: Double)](./init%28sampletime,atrate%29.md)
  Creates an audio time object with the specified timestamp and sample rate.
- [func extrapolateTime(fromAnchor: AVAudioTime) -> AVAudioTime?](./extrapolatetime%28fromanchor%29.md)
  Creates an audio time object by converting between host time and sample time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/init(audiotimestamp:samplerate:))*