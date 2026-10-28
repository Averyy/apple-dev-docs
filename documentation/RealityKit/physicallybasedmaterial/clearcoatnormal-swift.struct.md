# PhysicallyBasedMaterial.ClearcoatNormal

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines the clearcoat normal map texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ClearcoatNormal
```

## Overview

An entity in RealityKit can display a clearcoat, which is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. Use this object to specify a clearcoat normal and vary the normal used to calculate the clearcoat. This can be used to add imperfections and waviness to the clearcoat layer.

For information, see [`clearcoatNormal`](./clearcoatnormal-swift.property.md).

## Topics

### Initializers
- [init(CustomMaterial.ClearcoatNormal)](./clearcoatnormal-swift.struct/init%28_%29.md)
  Creates a clear coat normal object from a custom material’s clear coat normal property.
- [init(texture: PhysicallyBasedMaterial.Texture?)](./clearcoatnormal-swift.struct/init%28texture%29.md)
  Creates an object from a specified texture.
### Instance Properties
- [var texture: PhysicallyBasedMaterial.Texture?](./clearcoatnormal-swift.struct/texture.md)
  The material’s clearcoat normal map.
### Type Properties
- [static let textureSemantic: TextureResource.Semantic](./clearcoatnormal-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoatnormal-swift.struct)*