# lightingModel

**Framework**: RealityKit  
**Kind**: property

The lighting model to use when rendering this material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var lightingModel: LightingModel
```

#### Discussion

Must match the type of the surface output node in [`shaderGraph`](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md).

## See Also

- [var blendMode: MaterialParameterTypes.BlendMode?](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/blendmode.md)
  How materials using this program blend with content behind them.
- [var isColorDitheringEnabled: Bool](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/iscolorditheringenabled.md)
  Whether to dither color values before writing to the frame buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct/lightingmodel)*