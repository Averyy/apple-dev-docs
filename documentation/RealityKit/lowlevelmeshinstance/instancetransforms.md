# instanceTransforms

**Framework**: RealityKit  
**Kind**: property

The transform buffer for GPU instancing, or `nil` for single-instance rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var instanceTransforms: LowLevelInstanceTransformResource? { get }
```

#### Discussion

When non-`nil`, the renderer issues a single instanced draw call with `instanceTransforms.instanceCount` instances. Each entry is a model-to-local transform; the renderer multiplies it by `transform` to produce the final world transform: `transform * instanceTransforms[i]`.

## See Also

- [func setInstanceTransforms(LowLevelInstanceTransformResource?) throws(LowLevelRenderContextError)](lowlevelmeshinstance/setinstancetransforms(_:).md)
  Assigns or clears the transform buffer for GPU instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstance/instancetransforms)*