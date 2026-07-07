# geometryBindTransform

**Framework**: RealityKit  
**Kind**: property

The geometry bind transform applied to vertex positions before the joint skinning math.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var geometryBindTransform: simd_float4x4 { get nonmutating set }
```

#### Discussion

Defaults to `matrix_identity_float4x4`. Can be changed between `encode()` calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct/geometrybindtransform)*