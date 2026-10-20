# segments

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSArray<PHASEEnvelopeSegment *> * segments;
```

#### Discussion

The framework sets the value of this property to the [`init(startPoint:segments:)`](./init%28startpoint,segments%29.md) argument.

## See Also

### Inspecting the Envelope
- [func evaluate(x: Double) -> Double](./evaluate%28x%29.md)
  Provides the height of the envelope for an input value.
- [var startPoint: simd_double2](./startpoint.md)
  The starting point along the envelope’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/segments)*