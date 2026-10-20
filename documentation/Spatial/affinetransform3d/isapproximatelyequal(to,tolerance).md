# isApproximatelyEqual(to:tolerance:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether two transforms are equal within a specified tolerance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func isApproximatelyEqual(to other: AffineTransform3D, tolerance: Double = sqrt(.ulpOfOne)) -> Bool
```

## Parameters

- `other`: The right-hand side value.
- `tolerance`: A double-precision value that specifies the tolerance.

## See Also

### Comparing values
- [static func == (AffineTransform3D, AffineTransform3D) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/isapproximatelyequal(to:tolerance:))*