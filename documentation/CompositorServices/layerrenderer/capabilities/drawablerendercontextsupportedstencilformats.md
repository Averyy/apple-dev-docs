# drawableRenderContextSupportedStencilFormats

**Framework**: Compositor Services  
**Kind**: property

Returns the color format at the specified index in the layer capabilities.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var drawableRenderContextSupportedStencilFormats: [MTLPixelFormat] { get }
```

#### Return Value

The color format at the specified index.

#### Discussion

Use this function to determine the pixel arrangements and characteristics you can apply to the layer.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `index`: A zero-based index into the list of color formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/drawablerendercontextsupportedstencilformats)*