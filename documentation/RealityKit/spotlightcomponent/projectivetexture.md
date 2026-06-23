# SpotLightComponent.ProjectiveTexture

**Framework**: RealityKit  
**Kind**: struct

A component that specifies a map of a projective texture or cookie light to use for shadow mapping.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ProjectiveTexture
```

#### Overview

Cookie lights or projective lights in RealityKit are essentially a light mask added to our SpotLights that allows us to create a shadow that can illuminate an area uniformly by modifying the characteristics of the light. To illustrate the concept, we can think of a piece of gelatin paper wrapped around a light. The final illumination of the objects lit by this light will be a combination of the characteristics of the color of the light and the paper. Projective lights are available on devices with Apple6 GPU family feature support.

## Topics

### Creating a projective texture
- [init(texture: TextureResource, coordinateTransform: SpotLightComponent.ProjectiveTexture.TextureCoordinateTransform)](spotlightcomponent/projectivetexture/init(texture:coordinatetransform:).md)
  Creates a new instance with the specified texture and coordinate transform for scale and rotation
- [init(texture: TextureResource, scale: SIMD2<Float>)](spotlightcomponent/projectivetexture/init(texture:scale:).md)
  Creates a new instance with the specified texture and scale
### Transforming texture coordinates
- [var coordinateTransform: SpotLightComponent.ProjectiveTexture.TextureCoordinateTransform](spotlightcomponent/projectivetexture/coordinatetransform.md)
  The coordinate transform for the projective texture
- [SpotLightComponent.ProjectiveTexture.TextureCoordinateTransform](spotlightcomponent/projectivetexture/texturecoordinatetransform.md)
### Comparing projective textures
- [static func == (SpotLightComponent.ProjectiveTexture, SpotLightComponent.ProjectiveTexture) -> Bool](spotlightcomponent/projectivetexture/==(_:_:).md)
### Initializers
- [init(texture: TextureResource)](spotlightcomponent/projectivetexture/init(texture:).md)
  Creates a new instance with the specified texture
### Instance Properties
- [var texture: TextureResource](spotlightcomponent/projectivetexture/texture.md)
  The texture for the projective texture

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [SpotLightComponent.SurroundingsLight](spotlightcomponent/surroundingslight.md)
  A component that specifies that the spot light illuminates the physical and immersive environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/projectivetexture)*