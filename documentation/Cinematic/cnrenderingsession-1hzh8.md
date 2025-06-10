# CNRenderingSession

**Framework**: Cinematic  
**Kind**: class

An object representing the context in which rendering occurs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class CNRenderingSession
```

## Topics

### Structures
- [CNRenderingSession.Attributes](cnrenderingsession-1hzh8/attributes.md)
  The rendering session asset attributes.
- [CNRenderingSession.FrameAttributes](cnrenderingsession-1hzh8/frameattributes.md)
  Controls the focus distance and aperture of the rendering for the frames.
### Initializers
- [init(commandQueue: any MTLCommandQueue, sessionAttributes: CNRenderingSession.Attributes, preferredTransform: CGAffineTransform, quality: CNRenderingQuality)](cnrenderingsession-1hzh8/init(commandqueue:sessionattributes:preferredtransform:quality:).md)
  Intializes an object for a rendering session.
### Instance Properties
- [let commandQueue: any MTLCommandQueue](cnrenderingsession-1hzh8/commandqueue.md)
  The command queue of a Metal device that creates the command buffer.
- [let preferredTransform: CGAffineTransform](cnrenderingsession-1hzh8/preferredtransform.md)
  The preferred transform of the rendered image for display purposes.
- [let quality: CNRenderingQuality](cnrenderingsession-1hzh8/quality.md)
  The quality of rendering desired for a session.
- [let sessionAttributes: CNRenderingSession.Attributes](cnrenderingsession-1hzh8/sessionattributes.md)
  Rendering session attributes for a Cinematic asset.
### Instance Methods
- [func encodeRender(to: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer, destinationImage: CVPixelBuffer) -> Bool](cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationimage:).md)
- [func encodeRender(to: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer, destinationLuma: any MTLTexture, destinationChroma: any MTLTexture) -> Bool](cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationluma:destinationchroma:).md)
- [func encodeRender(to: any MTLCommandBuffer, frameAttributes: CNRenderingSession.FrameAttributes, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer, destinationRGBA: any MTLTexture) -> Bool](cnrenderingsession-1hzh8/encoderender(to:frameattributes:sourceimage:sourcedisparity:destinationrgba:).md)
### Type Properties
- [static var destinationPixelFormatTypes: [OSType]](cnrenderingsession-1hzh8/destinationpixelformattypes.md)
  A static number representing the video compositor’s required pixel buffer attributes context dictionary when implementing video compositing.
- [static var sourcePixelFormatTypes: [OSType]](cnrenderingsession-1hzh8/sourcepixelformattypes.md)
  The static pixel format types supported for the output destination.

## See Also

- [class CNAssetInfo](cnassetinfo-2ata2.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [class CNCompositionInfo](cncompositioninfo-7eunn.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8)*