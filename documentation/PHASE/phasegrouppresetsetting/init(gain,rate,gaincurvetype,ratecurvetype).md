# init(gain:rate:gainCurveType:rateCurveType:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a group preset setting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(gain: Double, rate: Double, gainCurveType: PHASECurveType, rateCurveType: PHASECurveType)
```

```objc
- (instancetype) initWithGain:(double) gain rate:(double) rate gainCurveType:(PHASECurveType) gainCurveType rateCurveType:(PHASECurveType) rateCurveType;
```

## Parameters

- `gain`: The volume of audio playback. See [`gain`](./gain.md).
- `rate`: The playback speed for audio. See [`rate`](./rate.md).
- `gainCurveType`: A rate of change for the setting’s volume.
- `rateCurveType`: A rate of change for the setting’s playback speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppresetsetting/init(gain:rate:gaincurvetype:ratecurvetype:))*