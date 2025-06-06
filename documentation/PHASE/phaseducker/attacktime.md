# attackTime

**Framework**: PHASE  
**Kind**: property

The amount of time for sound reduction to reach maximum strength.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var attackTime: Double { get }
```

## See Also

- [var gain: Double](phaseducker/gain.md)
  The amount of volume reduction.
- [var identifier: String](phaseducker/identifier.md)
  A unique value for the ducker.
- [var isActive: Bool](phaseducker/isactive.md)
  A Boolean value that determines whether the ducker reduces sound.
- [var attackCurve: PHASECurveType](phaseducker/attackcurve.md)
  A mathematical curve that shapes transition progress as sound reduction begins.
- [var releaseTime: Double](phaseducker/releasetime.md)
  The amount of time to transition from maximum sound reduction to no reduction.
- [var releaseCurve: PHASECurveType](phaseducker/releasecurve.md)
  A mathematical curve that shapes transition progress as sound reduction ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseducker/attacktime)*