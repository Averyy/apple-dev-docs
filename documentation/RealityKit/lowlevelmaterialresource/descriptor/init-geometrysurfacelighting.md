# init(geometry:surface:lighting:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor from the three shader stages.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(geometry: LowLevelMaterialResource.GeometryModifier, surface: LowLevelMaterialResource.SurfaceShader, lighting: LowLevelMaterialResource.LightingFunction)
```

## Parameters

- `geometry`: The vertex-stage geometry modifier.
- `surface`: The fragment-stage surface shader.
- `lighting`: The lighting evaluation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/descriptor/init(geometry:surface:lighting:))*