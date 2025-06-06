# supportedLayouts(options:)

**Framework**: Compositor Services  
**Kind**: method

Returns an array of texture layouts that the layer supports.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func supportedLayouts(options: LayerRenderer.Capabilities.SupportedLayoutsOptions) -> [LayerRenderer.Layout]
```

#### Return Value

An array of supported layouts. If the layer doesn’t support any layouts with the specified options, this function returns an empty array.

#### Discussion

Call this function to determine which texture layouts you can use for your content.

## Parameters

- `options`: Specific options you want the layouts to support. The function returns only layouts that support the specified options.

## See Also

- [LayerRenderer.Capabilities.SupportedLayoutsOptions](layerrenderer/capabilities/supportedlayoutsoptions.md)
  Options you can use to filter the supported layouts for a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedlayouts(options:))*