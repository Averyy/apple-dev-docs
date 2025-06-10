# scale

**Framework**: RealityKit  
**Kind**: property

The reflectiveness value for the entire entity or a multiplier for the metallic texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
var scale: Float
```

#### Discussion

This property is an input to your material’s surface shader. Although you can choose how to use the `scale` value in your shader, RealityKit provides this property to control the reflectiveness of the entire entity when there’s no texture, or to function as a multiplier to the values you sample from the texture.

## See Also

- [var texture: CustomMaterial.Texture?](custommaterial/metallic-swift.struct/texture.md)
  The reflectiveness as a UV-mapped image texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/metallic-swift.struct/scale)*