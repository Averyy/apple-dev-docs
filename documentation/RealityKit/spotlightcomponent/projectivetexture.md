# SpotLightComponent.ProjectiveTexture

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A component that specifies a map of a projective texture or cookie light to use for shadow mapping.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ProjectiveTexture
```

## Overview

Cookie lights or projective lights in RealityKit are essentially a light mask added to our SpotLights that allows us to create a shadow that can illuminate an area uniformly by modifying the characteristics of the light. To illustrate the concept, we can think of a piece of gelatin paper wrapped around a light. The final illumination of the objects lit by this light will be a combination of the characteristics of the color of the light and the paper. Projective lights are available on devices with Apple6 GPU family feature support.

## Topics

### Creating a projective texture
- [init(texture: TextureResource, coordinateTransform: SpotLightComponent.ProjectiveTexture.TextureCoordinateTransform)](./projectivetexture/init%28texture,coordinatetransform%29.md)
  Creates a new instance with the specified texture and coordinate transform for scale and rotation
- [init(texture: TextureResource, scale: SIMD2<Float>)](./projectivetexture/init%28texture,scale%29.md)
  Creates a new instance with the specified texture and scale
### Transforming texture coordinates
- [var coordinateTransform: SpotLightComponent.ProjectiveTexture.TextureCoordinateTransform](./projectivetexture/coordinatetransform.md)
  The coordinate transform for the projective texture
- [SpotLightComponent.ProjectiveTexture.TextureCoordinateTransform](./projectivetexture/texturecoordinatetransform.md)
### Comparing projective textures
- [static func == (SpotLightComponent.ProjectiveTexture, SpotLightComponent.ProjectiveTexture) -> Bool](./projectivetexture/eqeq%28_,_%29.md)
### Initializers
- [init(texture: TextureResource)](./projectivetexture/init%28texture%29.md)
  Creates a new instance with the specified texture
### Instance Properties
- [var texture: TextureResource](./projectivetexture/texture.md)
  The texture for the projective texture

## Relationships

### Conforms To
- [Component](../component.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Defining the light contribution
- [SpotLightComponent.SurroundingsLight](./surroundingslight.md)
  A component that specifies that the spot light illuminates the physical and immersive environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/projectivetexture)*