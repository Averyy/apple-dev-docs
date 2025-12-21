# apply(_:)

**Framework**: Spatial  
**Kind**: method

Applies a pose.

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
mutating func apply(_ pose: Pose3DFloat)
```

## Parameters

- `pose`: The pose.   This function rotate’s the ray’s direction by the pose’s rotation and sets the ray’s origin to the pose’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/apply(_:))*