# bounds

**Framework**: RealityKit  
**Kind**: property

The bounding box that defines the clipping region in the entity’s local coordinate space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var bounds: BoundingBox
```

#### Discussion

Content outside this bounding box will be clipped (hard edge or faded out based on feathering). The bounds are defined relative to the entity’s origin and are affected by the entity’s transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingcomponent/bounds)*