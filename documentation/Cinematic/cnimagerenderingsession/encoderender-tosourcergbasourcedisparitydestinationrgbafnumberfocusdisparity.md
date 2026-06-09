# encodeRender(to:sourceRGBA:sourceDisparity:destinationRGBA:fNumber:focusDisparity:)

**Framework**: Cinematic  
**Kind**: method

Encode a command to render a shallow depth of field (SDoF) image to a metal texture

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
func encodeRender(to commandBuffer: any MTLCommandBuffer, sourceRGBA: any MTLTexture, sourceDisparity: any MTLTexture, destinationRGBA: any MTLTexture, fNumber: Float, focusDisparity: Float) -> Bool
```

#### Return Value

YES if encoding succeeded; NO if required resources are unavailable or if the provided textures are incompatible.

## Parameters

- `commandBuffer`: The Metal command buffer on which to encode the command
- `sourceRGBA`: A color texture to which the effect should be applied. Texture must be in linear color space. The width and height must match those of destinationRGBA.
- `sourceDisparity`: The texture with the disparity
- `destinationRGBA`: The texture to which the SDoF image is rendered. Texture must be in linear color space. Must have the same dimensions as sourceRGBA.
- `fNumber`: The f-stop value which inversely affects the aperture used to render the image. A smaller f/ number results in larger bokeh and a shallower depth of field in the rendered image.
- `focusDisparity`: The disparity value which represents the focus plane at which the rendered image should be in focus. A larger disparity results in the focus plane being closer to the camera. The scale and offset of disparity is not defined. It is best practice to obtain disparity values from detections or by interpolation between known disparity values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsession/encoderender(to:sourcergba:sourcedisparity:destinationrgba:fnumber:focusdisparity:))*