# supportedColorFormats

**Framework**: Compositor Services  
**Kind**: property

An array of color formats that the layer supports for its textures.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var supportedColorFormats: [MTLPixelFormat] { get }
```

#### Discussion

The pixel formats in this property tell you which pixel arrangements and characteristics the layer supports for its color textures.

## See Also

- [var supportedDepthFormats: [MTLPixelFormat]](layerrenderer/capabilities/supporteddepthformats.md)
  The list of depth formats that the layer supports


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedcolorformats)*