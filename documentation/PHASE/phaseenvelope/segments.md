# segments

**Framework**: PHASE  
**Kind**: property

An array of the envelope’s segments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var segments: [PHASEEnvelopeSegment] { get }
```

#### Discussion

The framework sets the value of this property to the [`init(startPoint:segments:)`](phaseenvelope/init(startpoint:segments:).md) argument.

## See Also

- [func evaluate(x: Double) -> Double](phaseenvelope/evaluate(x:).md)
  Provides the height of the envelope for an input value.
- [var startPoint: simd_double2](phaseenvelope/startpoint.md)
  The starting point along the envelope’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/segments)*