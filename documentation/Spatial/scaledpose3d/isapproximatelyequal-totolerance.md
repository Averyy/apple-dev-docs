# isApproximatelyEqual(to:tolerance:)

**Framework**: Spatial  
**Kind**: method

Returns a Boolean value that indicates whether two scaled poses are equal within a specified tolerance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
func isApproximatelyEqual(to other: ScaledPose3D, tolerance: Double = sqrt(.ulpOfOne)) -> Bool
```

## See Also

- [static func == (ScaledPose3D, ScaledPose3D) -> Bool](scaledpose3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/isapproximatelyequal(to:tolerance:))*