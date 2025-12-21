# isApproximatelyEqual(to:tolerance:)

**Framework**: Spatial  
**Kind**: method

Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func isApproximatelyEqual(to other: AffineTransform3DFloat, tolerance: Float = sqrt(.ulpOfOne)) -> Bool
```

## Parameters

- `tolerance`: The tolerance of the comparison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3dfloat/isapproximatelyequal(to:tolerance:))*