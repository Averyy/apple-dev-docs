# rate

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The playback speed for audio.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var rate: Double { get }
```

```objc
@property (nonatomic, readonly) double rate;
```

#### Discussion

The framework sets the value to the [`init(gain:rate:gainCurveType:rateCurveType:)`](./init%28gain,rate,gaincurvetype,ratecurvetype%29.md) parameter.

## See Also

### Setting Playback Speed
- [var rateCurveType: PHASECurveType](./ratecurvetype.md)
  A rate of change for the setting’s playback speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting/rate)*