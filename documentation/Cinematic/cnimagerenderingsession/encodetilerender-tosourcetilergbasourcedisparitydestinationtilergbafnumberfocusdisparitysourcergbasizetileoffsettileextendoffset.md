# encodeTileRender(to:sourceTileRGBA:sourceDisparity:destinationTileRGBA:fNumber:focusDisparity:sourceRGBASize:tileOffset:tileExtendOffset:)

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
func encodeTileRender(to commandBuffer: any MTLCommandBuffer, sourceTileRGBA: any MTLTexture, sourceDisparity: any MTLTexture, destinationTileRGBA: any MTLTexture, fNumber: Float, focusDisparity: Float, sourceRGBASize: CGSize, tileOffset: CGPoint, tileExtendOffset: CGPoint) -> Bool
```

#### Return Value

YES if encoding succeeded; NO if required resources are unavailable or if the provided parameters are incompatible.

#### Discussion

Tiled rendering avoids allocating a full-resolution texture for large images. The source tile must be larger than the destination tile (the “extend” region) so the renderer has enough surrounding pixel context to correctly compute bokeh near tile edges. Use `minimumTileExtendRectForTileRect:sourceRGBASize:` to compute the required extended source rect.

## Parameters

- `commandBuffer`: The Metal command buffer on which to encode the command
- `sourceTileRGBA`: A color texture to which the effect should be applied. Texture must be in linear color space. Its origin in the full image is given by tileExtendOffset.
- `sourceDisparity`: The texture with the disparity. This texture is not tiled.
- `destinationTileRGBA`: The texture to which the SDoF image is rendered. Texture must be in linear color space. Its dimensions define the tile size. Its origin in the full image is given by `tileOffset`.
- `fNumber`: The f-stop value which inversely affects the aperture used to render the image. A smaller f/ number results in larger bokeh and a shallower depth of field in the rendered image.
- `focusDisparity`: The disparity value which represents the focus plane at which the rendered image should be in focus. A larger disparity results in the focus plane being closer to the camera. The scale and offset of disparity is not defined. It is best practice to obtain disparity values from detections or by interpolation between known disparity values.
- `sourceRGBASize`: The width and height of the full (un-tiled) source image.
- `tileOffset`: The pixel-coordinate origin of the destination tile within the full image.
- `tileExtendOffset`: The pixel-coordinate origin of the extended source tile within the full image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsession/encodetilerender(to:sourcetilergba:sourcedisparity:destinationtilergba:fnumber:focusdisparity:sourcergbasize:tileoffset:tileextendoffset:))*