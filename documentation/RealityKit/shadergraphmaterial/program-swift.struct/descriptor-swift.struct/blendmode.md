# blendMode

**Framework**: RealityKit  
**Kind**: property

How materials using this program blend with content behind them.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var blendMode: MaterialParameterTypes.BlendMode?
```

#### Discussion

When `nil`, the material renders opaque.

## See Also

- [var lightingModel: LightingModel](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/lightingmodel.md)
  The lighting model to use when rendering this material.
- [var isColorDitheringEnabled: Bool](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/iscolorditheringenabled.md)
  Whether to dither color values before writing to the frame buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct/blendmode)*