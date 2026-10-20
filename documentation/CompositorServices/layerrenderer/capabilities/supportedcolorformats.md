# supportedColorFormats

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

An array of color formats that the layer supports for its textures.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use supportedColorFormats(options: SupportedColorFormatsOptions) instead.

## Declaration

```swift
var supportedColorFormats: [MTLPixelFormat] { get }
```

#### Discussion

The pixel formats in this property tell you which pixel arrangements and characteristics the layer supports for its color textures.

## See Also

### Getting the supported formats
- [var supportedDepthFormats: [MTLPixelFormat]](./supporteddepthformats.md)
  The list of depth formats that the layer supports


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedcolorformats)*