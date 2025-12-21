# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Returns the primitive that results from applying a pose to the primitive.

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
func unapplying(_ pose: Pose3DFloat) -> Rect3DFloat
```

#### Discussion

- Returns The transformed primitive.

> **Note**: The pose’s rotation angle must be zero, otherwise this function returns `self`.

## Parameters

- `pose`: The pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/unapplying(_:)-7w0uc)*