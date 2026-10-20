# fadeGain(gain:duration:curveType:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Adjusts the volume of the sounds in a group gradually.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func fadeGain(gain: Double, duration: Double, curveType: PHASECurveType)
```

```objc
- (void) fadeGain:(double) gain duration:(double) duration curveType:(PHASECurveType) curveType;
```

## Parameters

- `gain`: The target volume.
- `duration`: The total time to complete the volume adjustment. The framework scales this value by [`unitsPerSecond`](../phaseengine/unitspersecond.md).
- `curveType`: A selection that specifies a mathematical curve that shapes the volume adjustment over time.

## See Also

### Conrolling Loudness
- [var gain: Double](./gain.md)
  Modifies the volume of the group’s sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup/fadegain(gain:duration:curvetype:))*