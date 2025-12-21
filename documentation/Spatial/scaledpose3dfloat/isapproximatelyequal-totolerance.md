# isApproximatelyEqual(to:tolerance:)

**Framework**: Spatial  
**Kind**: method

Returns a Boolean value that indicates whether two scaled poses are equal within a specified tolerance.

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
func isApproximatelyEqual(to other: ScaledPose3DFloat, tolerance: Float = sqrt(.ulpOfOne)) -> Bool
```

## Parameters

- `other`: The second  scaled pose.
- `tolerance`: The tolerance of the comparison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3dfloat/isapproximatelyequal(to:tolerance:))*