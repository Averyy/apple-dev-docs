# evaluate(x:)

**Framework**: PHASE  
**Kind**: method

Provides the height of the envelope for an input value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func evaluate(x: Double) -> Double
```

#### Return Value

The curve’s height for the argument  value.

## Parameters

- `x`: A value within the envelope’s domain. The envelope clamps this parameter to a value within  .

## See Also

- [var segments: [PHASEEnvelopeSegment]](phaseenvelope/segments.md)
  An array of the envelope’s segments.
- [var startPoint: simd_double2](phaseenvelope/startpoint.md)
  The starting point along the envelope’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/evaluate(x:))*