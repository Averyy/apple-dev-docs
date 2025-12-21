# makeConfiguration(capabilities:configuration:)

**Framework**: Compositor Services  
**Kind**: method  
**Required**: Yes

Creates and returns a type that contains the rendering options for Compositor Services to use when configuring a layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeConfiguration(capabilities: LayerRenderer.Capabilities, configuration: inout LayerRenderer.Configuration)
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

In your implementation of this method, modify the `configuration` parameter to specify the Metal texture formats and layouts you want to use during rendering. Verify that your preferred choices are available by checking the supported options using the information in the `capabilities` parameter.

## Parameters

- `capabilities`: The supported capabilities of the current device.   Use these values to validate any choices you apply to the   parameter.
- `configuration`: The default set of configuration options.   Modify this type to specify the options you want to use during rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/compositorlayerconfiguration/makeconfiguration(capabilities:configuration:))*