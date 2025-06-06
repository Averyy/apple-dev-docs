# supportedDepthFormats

**Framework**: Compositor Services  
**Kind**: property

The list of depth formats that the layer supports

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var supportedDepthFormats: [MTLPixelFormat] { get }
```

#### Discussion

The pixel formats in this property tell you which pixel arrangements and characteristics the layer supports for its depth textures.

## See Also

- [var supportedColorFormats: [MTLPixelFormat]](layerrenderer/capabilities/supportedcolorformats.md)
  An array of color formats that the layer supports for its textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supporteddepthformats)*