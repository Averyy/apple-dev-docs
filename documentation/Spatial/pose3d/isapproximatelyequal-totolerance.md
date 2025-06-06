# isApproximatelyEqual(to:tolerance:)

**Framework**: Spatial  
**Kind**: method

Returns a Boolean value that indicates whether two poses are equal within a specified tolerance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func isApproximatelyEqual(to other: Pose3D, tolerance: Double = sqrt(.ulpOfOne)) -> Bool
```

## Parameters

- `other`: The right-hand side value.
- `tolerance`: A double-precision value that specifies the tolerance.

## See Also

- [static func == (Pose3D, Pose3D) -> Bool](pose3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/isapproximatelyequal(to:tolerance:))*