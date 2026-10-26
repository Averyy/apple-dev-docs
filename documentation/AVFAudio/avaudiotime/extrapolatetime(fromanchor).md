# extrapolateTime(fromAnchor:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Creates an audio time object by converting between host time and sample time.

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
func extrapolateTime(fromAnchor anchorTime: AVAudioTime) -> AVAudioTime?
```

```objc
- (AVAudioTime *) extrapolateTimeFromAnchor:(AVAudioTime *) anchorTime;
```

#### Return Value

A new [`AVAudioTime`](../avaudiotime.md) instance.

#### Discussion

If `anchorTime` is an `AVAudioTime` instance where both host time and sample time are valid, and the receiver is another timestamp where only one of the two is valid, this method returns a new `AVAudioTime`. It copies it from the receiver, where the anchor provides additional valid fields.

The `anchorTime` value must have a valid host time and sample time, and self must have sample rate and at least one valid host time or sample time. Otherwise, this method returns `nil`.

```objc
// time0 has a valid audio sample representation, but no host time representation.
AVAudioTime *time0 = [AVAudioTime timeWithSampleTime: 0.0 atRate: 44100.0];
// anchor has a valid host time representation and sample time representation.
AVAudioTime *anchor = [node currentTime];
// fill in  valid host time representation
AVAudioTime *fullTime = [sampleTime extrapolateTimeFromAnchor: sampleTime];
```

## Parameters

- `anchorTime`: An audio time instance with a more complete timestamp than that of the receiver (self).

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
- [+ timeWithHostTime:sampleTime:atRate:](./timewithhosttime_sampletime_atrate_.md)
  Creates an audio time object with the specified host time, sample time, and sample rate.
- [+ timeWithSampleTime:atRate:](./timewithsampletime_atrate_.md)
  Creates an audio time object with the specified sample time and sample rate.
- [+ timeWithHostTime:](./timewithhosttime_.md)
  Creates an audio time object with the specified host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime/extrapolatetime(fromanchor:))*