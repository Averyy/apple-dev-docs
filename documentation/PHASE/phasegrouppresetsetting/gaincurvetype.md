# gainCurveType

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A rate of change for the setting’s volume.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gainCurveType: PHASECurveType { get }
```

```objc
@property (nonatomic, readonly) PHASECurveType gainCurveType;
```

## Discussion

The framework sets the value to the [`init(gain:rate:gainCurveType:rateCurveType:)`](./init%28gain,rate,gaincurvetype,ratecurvetype%29.md) parameter.

## See Also

### Setting Loudness
- [var gain: Double](./gain.md)
  The volume of audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting/gaincurvetype)*