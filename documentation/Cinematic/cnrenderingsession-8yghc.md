# CNRenderingSession

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object representing the context in which rendering occurs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNRenderingSession : NSObject
```

## Topics

### Instance Properties
- [commandQueue](./cnrenderingsession-8yghc/commandqueue.md)
  The command queue of a Metal device that creates the command buffer.
- [preferredTransform](./cnrenderingsession-8yghc/preferredtransform.md)
  The preferred transform of the rendered image for display purposes.
- [quality](./cnrenderingsession-8yghc/quality.md)
  The quality of rendering desired for a session.
- [sessionAttributes](./cnrenderingsession-8yghc/sessionattributes.md)
  Rendering session attributes for a Cinematic asset.
### Instance Methods
- [- encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationImage:](./cnrenderingsession-8yghc/encoderendertocommandbuffer_frameattributes_sourceimage_sourcedisparity_destinationimage_.md)
  Encodes a command to render a shallow depth of field (SDoF) image to a pixel buffer.
- [- encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationLuma:destinationChroma:](./cnrenderingsession-8yghc/encoderendertocommandbuffer_frameattributes_sourceimage_sourcedisparity_destinationluma_destinationchroma_.md)
  Encodes a command to render a shallow depth of field (SDoF) image to two metal textures as luma and chroma.
- [- encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationRGBA:](./cnrenderingsession-8yghc/encoderendertocommandbuffer_frameattributes_sourceimage_sourcedisparity_destinationrgba_.md)
  Encodes a command to render a shallow depth of field (SDoF) image to a metal texture as RGBA.
- [- initWithCommandQueue:sessionAttributes:preferredTransform:quality:](./cnrenderingsession-8yghc/initwithcommandqueue_sessionattributes_preferredtransform_quality_.md)
  Intializes an object for a rendering session.
### Type Properties
- [destinationPixelFormatTypes](./cnrenderingsession-8yghc/destinationpixelformattypes.md)
  A static number representing the video compositor’s required pixel buffer attributes context dictionary when implementing video compositing.
- [sourcePixelFormatTypes](./cnrenderingsession-8yghc/sourcepixelformattypes.md)
  The pixel format types supported for the output destination.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Reading and rendering
- [CNAssetInfo](./cnassetinfo-8ja4t.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [CNCompositionInfo](./cncompositioninfo-vzoh.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [CNRenderingSessionAttributes](./cnrenderingsessionattributes.md)
  A structure for movie-wide attributes required for proper rendering.
- [CNRenderingSessionFrameAttributes](./cnrenderingsessionframeattributes.md)
  Creates an object with the per frame attributes that control the appearance of a single frame of the Cinematic movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-8yghc)*