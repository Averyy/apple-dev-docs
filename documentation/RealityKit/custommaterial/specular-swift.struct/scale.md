# scale

**Framework**: RealityKit  
**Kind**: property

The specular value for the entire entity or a multiplier for values sampled from the material’s texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
var scale: Float
```

#### Discussion

If [`texture`](custommaterial/specular-swift.struct/texture.md) is `nil`, RealityKit uses this value for the opacity of the entire material. If [`texture`](custommaterial/specular-swift.struct/texture.md) isn’t `nil`, RealityKit multiplies the value sampled from [`texture`](custommaterial/specular-swift.struct/texture.md) by this property to calculate the final opacity values.

## See Also

- [var texture: CustomMaterial.Texture?](custommaterial/specular-swift.struct/texture.md)
  The specular value as a UV-mapped image texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/specular-swift.struct/scale)*