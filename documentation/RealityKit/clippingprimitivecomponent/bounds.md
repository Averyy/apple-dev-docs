# bounds

**Framework**: RealityKit  
**Kind**: property

The bounding box that defines the clipping region in the entity’s local coordinate space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var bounds: BoundingBox
```

#### Discussion

Content outside this bounding box will be clipped (hard edge or faded out based on feathering). The bounds are defined relative to the entity’s origin and are affected by the entity’s transform.

Default value is a zero-size bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent/bounds)*