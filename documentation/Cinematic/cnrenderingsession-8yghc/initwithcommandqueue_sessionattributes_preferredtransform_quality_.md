# initWithCommandQueue:sessionAttributes:preferredTransform:quality:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Intializes an object for a rendering session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithCommandQueue:(id<MTLCommandQueue>) commandQueue sessionAttributes:(CNRenderingSessionAttributes *) sessionAttributes preferredTransform:(CGAffineTransform) preferredTransform quality:(CNRenderingQuality) quality;
```

## Parameters

- `commandQueue`: The command queue of a metal device that creates the command buffer.
- `sessionAttributes`: Rendering session attributes loaded from a Cinematic asset.
- `preferredTransform`: The preferred transform of the rendered image for display purposes. Always the identity transform or a multiple of a 90º rotation with no scaling.
- `quality`: The quality of rendering desired for a session. Quality levels include thumbnail, preview, and three export quality levels. You can create more than one session for the same video with different quality levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-8yghc/initwithcommandqueue:sessionattributes:preferredtransform:quality:)*