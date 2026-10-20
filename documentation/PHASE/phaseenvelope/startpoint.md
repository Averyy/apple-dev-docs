# startPoint

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The starting point along the envelope’s duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var startPoint: simd_double2 { get }
```

```objc
@property (nonatomic, readonly) simd_double2 startPoint;
```

#### Discussion

The framework sets the value of this property to the [`init(startPoint:segments:)`](./init%28startpoint,segments%29.md) argument.

## See Also

### Inspecting the Envelope
- [func evaluate(x: Double) -> Double](./evaluate%28x%29.md)
  Provides the height of the envelope for an input value.
- [var segments: [PHASEEnvelopeSegment]](./segments.md)
  An array of the envelope’s segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/startpoint)*