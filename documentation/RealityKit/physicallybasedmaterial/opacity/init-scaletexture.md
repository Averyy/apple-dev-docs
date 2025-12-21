# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates an opacity object using a single value or a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(scale: Float = 1.0, texture: PhysicallyBasedMaterial.Texture? = nil)
```

#### Discussion

This initializer allows you to create an instance using either a single value for the entire material or a UV-mapped image. If `texture` is non-`nil`, RealityKit uses that image to determine the material’s opacity and ignores `scale`. If `texture` is `nil`, then it uses `scale` for the entire material.

## Parameters

- `scale`: The opacity value for the entire material.
- `texture`: The opacity values as a UV-mapped image.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/opacity/init(floatliteral:).md)
  Creates an opacity object using a single value.
- [init(CustomMaterial.Opacity)](physicallybasedmaterial/opacity/init(_:).md)
  Creates an opacity object using a custom material’s opacity property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/opacity/init(scale:texture:))*