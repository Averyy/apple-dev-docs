# init(texture:level:slice:depthPlane:)

**Framework**: RealityKit  
**Kind**: init

Creates a texture reference with the given texture, mip level, slice, and depth plane.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(texture: any MTLTexture, level: Int = 0, slice: Int = 0, depthPlane: Int = 0)
```

## Parameters

- `texture`: The underlying Metal texture.
- `level`: The mipmap level of the texture to use. Defaults to `0`.
- `slice`: The slice of the texture to use. Defaults to `0`.
- `depthPlane`: The depth plane of the texture to use. Defaults to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/output-swift.struct/texture/init(texture:level:slice:depthplane:))*