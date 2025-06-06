# endPoint

**Framework**: PHASE  
**Kind**: property

A point that identifies the end of the segment along the envelope.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var endPoint: simd_double2 { get set }
```

#### Discussion

The framework connects this property to the prior segment’s end point, or the envelope [`startPoint`](phaseenvelope/startpoint.md), in the case of the first segment.

## See Also

- [var curveType: PHASECurveType](phaseenvelopesegment/curvetype.md)
  A curve along the envelope that shapes the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelopesegment/endpoint)*