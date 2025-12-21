# supportedColorFormats(options:)

**Framework**: Compositor Services  
**Kind**: method

Returns an array of formats that the layer supports for its color textures

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func supportedColorFormats(options: LayerRenderer.Capabilities.SupportedColorFormatsOptions) -> [MTLPixelFormat]
```

#### Discussion

Call this function to determine which pixel arrangements and characteristics the layer supports for its color textures.

## Parameters

- `options`: Specific options you want the formats of the color textures to be supported with.   The function returns only color formats that are supported with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedcolorformats(options:))*