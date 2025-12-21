# provideImage(to:commandBuffer:originx:originy:width:height:userInfo:)

**Framework**: Objective-C Runtime  
**Kind**: method

An optional method that an image provider object way implement.
With this method, the provider object can use the Metal API to provide pixel
data into a MTLTexture when the image object is rendered.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func provideImage(to texture: any MTLTexture, commandBuffer: any MTLCommandBuffer, originx: Int, originy: Int, width: Int, height: Int, userInfo info: Any?)
```

#### Discussion

The implementation should provide pixels for the requested sub-rect `x,y,width,height` of the image. The sub-rect is in defined in the image’s local coordinate space, where the origin is relative to the top left corner of the image.

The work to fill the `MTLTexture` should be encoded on the specified `commandBuffer`.
If the implementation uses its own commandBuffer, then it should call `waitUntilCompleted` before returning. If the texture is surface-backed then you only need to call `waitUntilScheduled` before returning.

By default, this method will be called to request the full image regardless of what sub-rect is needed for the current render. In this case the requested `x,y,width,height` will be `0,0,imageWidth,imageHeight`

If the `kCIImageProviderTileSize` option is specified when the `CIImage` was created, then this method may be called once for each tile that is needed for the current render.

## Parameters

- `texture`: The   into which the provider should copy the pixels for the requested sub-rect.
- `commandBuffer`: The   that the provider should use encoded the copy.
- `originx`: The x origin of the requested sub-rect relative to the upper left corner of the image.
- `originy`: The y origin of the requested sub-rect relative to the upper left corner of the image.
- `width`: The width of the requested sub-rect.
- `height`: The height of the requested sub-rect.
- `info`: The value of the `kCIImageProviderTileSize /CIImage/imageWithImageProvider:size::format:colorSpace:options:``   * ``/CIImage/initWithImageProvider:size::format:colorSpace:options:``


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/provideimage(to:commandbuffer:originx:originy:width:height:userinfo:))*