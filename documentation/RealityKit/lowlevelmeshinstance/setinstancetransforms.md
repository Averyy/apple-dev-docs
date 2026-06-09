# setInstanceTransforms(_:)

**Framework**: RealityKit  
**Kind**: method

Assigns or clears the transform buffer for GPU instancing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func setInstanceTransforms(_ instanceTransforms: LowLevelInstanceTransformResource?) throws(LowLevelRenderContextError)
```

#### Discussion

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if `instanceTransforms` is incompatible with this instance.

## Parameters

- `instanceTransforms`: The transform buffer to assign, or `nil` to revert to single-instance rendering.

## See Also

- [var instanceTransforms: LowLevelInstanceTransformResource?](lowlevelmeshinstance/instancetransforms.md)
  The transform buffer for GPU instancing, or `nil` for single-instance rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstance/setinstancetransforms(_:))*