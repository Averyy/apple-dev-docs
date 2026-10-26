# encodeRenderToCommandBuffer:frameAttributes:sourceImage:sourceDisparity:destinationImage:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Encodes a command to render a shallow depth of field (SDoF) image to a pixel buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (BOOL) encodeRenderToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer frameAttributes:(CNRenderingSessionFrameAttributes *) frameAttributes sourceImage:(CVPixelBufferRef) sourceImage sourceDisparity:(CVPixelBufferRef) sourceDisparity destinationImage:(CVPixelBufferRef) destinationImage;
```

## Parameters

- `commandBuffer`: The metal command buffer on which to encode the command.
- `frameAttributes`: Controls the focus distance and aperture of the rendering.
- `sourceImage`: A pixel buffer read from the cinematicVideoTrack.
- `sourceDisparity`: A pixel buffer read from the cinematicDisparityTrack.
- `destinationImage`: The rendered pixel buffer of the SDoF image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-8yghc/encoderendertocommandbuffer:frameattributes:sourceimage:sourcedisparity:destinationimage:)*