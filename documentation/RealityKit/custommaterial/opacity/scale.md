# scale

**Framework**: RealityKit  
**Kind**: property

The amount of opacity specified as a single value.

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

If [`texture`](custommaterial/opacity/texture.md) is `nil`, RealityKit uses this value for the opacity of the entire material. If [`texture`](custommaterial/opacity/texture.md) isn’t `nil`, RealityKit multiplies the value sampled from [`texture`](custommaterial/opacity/texture.md) by this property to calculate the final opacity values.

## See Also

- [var texture: CustomMaterial.Texture?](custommaterial/opacity/texture.md)
  The amount of opacity specified using a UV-mapped image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/opacity/scale)*