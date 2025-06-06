# fadeRate(rate:duration:curveType:)

**Framework**: PHASE  
**Kind**: method

Adjusts the playback speed of the sounds in a group gradually.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func fadeRate(rate: Double, duration: Double, curveType: PHASECurveType)
```

## Parameters

- `rate`: The target playback speed.
- `duration`: The total time to adjust the playback speed. The framework scales this value by  .
- `curveType`: A selection that specifies a mathematical curve that shapes the playback speed adjustment over time.

## See Also

- [var rate: Double](phasegroup/rate.md)
  The group’s playback speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup/faderate(rate:duration:curvetype:))*