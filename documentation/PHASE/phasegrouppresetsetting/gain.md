# gain

**Framework**: PHASE  
**Kind**: property

The volume of audio playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gain: Double { get }
```

#### Discussion

The framework sets the value to the [`init(gain:rate:gainCurveType:rateCurveType:)`](phasegrouppresetsetting/init(gain:rate:gaincurvetype:ratecurvetype:).md) parameter, clamped to the range between `0` and `1`. A value of `0` silences the audio and `1` doesn’t modify the audio’s original volume.

## See Also

- [var gainCurveType: PHASECurveType](phasegrouppresetsetting/gaincurvetype.md)
  A rate of change for the setting’s volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting/gain)*