# isEqual(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Indicates whether the audio format instance and a specified object are functionally equivalent.

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
func isEqual(_ object: Any) -> Bool
```

```objc
- (BOOL) isEqual:(id) object;
```

#### Return Value

A Boolean value of [`true`](../../Swift/true.md) if the receiver and `object` are equal; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The PCM format ignores interleaveness for mono.

The method ignores the differences in the [`AudioStreamBasicDescription`](../../CoreAudioTypes/audiostreambasicdescription.md) alignment and packedness when they’re not significant. For example, with one channel, 2 bytes per frame, 16 bits per channel, and neither alignment, the format is implicit packedness and the method can interpret it as either high- or low-aligned.

For [`AVAudioChannelLayout`](../avaudiochannellayout.md), the method considers a layout with the standard mono or stereo tag to be equivalent to a `nil` layout.

Otherwise, the method compares the layouts for equality.

## Parameters

- `object`: The object to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioformat/isequal(_:))*