# supportedDepthFormats

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The list of depth formats that the layer supports

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var supportedDepthFormats: [MTLPixelFormat] { get }
```

#### Discussion

The pixel formats in this property tell you which pixel arrangements and characteristics the layer supports for its depth textures.

## See Also

### Getting the supported formats
- [var supportedColorFormats: [MTLPixelFormat]](./supportedcolorformats.md)
  An array of color formats that the layer supports for its textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supporteddepthformats)*