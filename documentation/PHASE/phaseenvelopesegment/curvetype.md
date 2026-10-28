# curveType

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A curve along the envelope that shapes the segment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var curveType: PHASECurveType { get set }
```

```objc
@property (nonatomic, assign) PHASECurveType curveType;
```

## Discussion

The option you choose for this property determines the segment’s y_-_value rate of change along the input.

## See Also

### Shaping a Segment
- [var endPoint: simd_double2](./endpoint.md)
  A point that identifies the end of the segment along the envelope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelopesegment/curvetype)*