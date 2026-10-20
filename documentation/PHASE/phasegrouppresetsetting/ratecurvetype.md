# rateCurveType

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A rate of change for the setting’s playback speed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var rateCurveType: PHASECurveType { get }
```

```objc
@property (nonatomic, readonly) PHASECurveType rateCurveType;
```

#### Discussion

The framework sets the value to the [`init(gain:rate:gainCurveType:rateCurveType:)`](./init%28gain,rate,gaincurvetype,ratecurvetype%29.md) parameter.

## See Also

### Setting Playback Speed
- [var rate: Double](./rate.md)
  The playback speed for audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting/ratecurvetype)*