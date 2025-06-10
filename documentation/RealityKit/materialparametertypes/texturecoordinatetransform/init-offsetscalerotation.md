# init(offset:scale:rotation:)

**Framework**: RealityKit  
**Kind**: init

Creates a texture coordinate transform object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(offset: SIMD2<Float> = .init(), scale: SIMD2<Float> = .init(1, 1), rotation: Float = 0.0)
```

## Parameters

- `offset`: The amount to offset the UV texture coordinates.
- `scale`: The amount to scale the UV texture coordinates.
- `rotation`: The amount to rotate the UV texture coordinates in   radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialparametertypes/texturecoordinatetransform/init(offset:scale:rotation:))*