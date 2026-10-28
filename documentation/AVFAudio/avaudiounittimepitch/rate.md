# rate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The playback rate of the input signal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rate: Float { get set }
```

```objc
@property (nonatomic) float rate;
```

## Discussion

The default value is 1.0. The range of supported values is `1/32` to `32.0`.

## See Also

### Adjusting pitch and rate
- [var overlap: Float](./overlap.md)
  The amount of overlap between segments of the input audio signal.
- [var pitch: Float](./pitch.md)
  The amount to use to pitch shift the input signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch/rate)*