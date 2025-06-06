# cameraGrainTexture

**Framework**: ARKit  
**Kind**: property

A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var cameraGrainTexture: (any MTLTexture)? { get }
```

#### Discussion

Camera grain enhances the visual cohesion of the real and augmented aspects of your user experience by enabling your app’s virtual content to take on similar image noise characteristics that naturally occur in the camera feed.

![Screenshot showing the before and after cases of applying image noise to an app’s virtual content.](https://docs-assets.developer.apple.com/published/91ac97857a79016f3be51942ca95e735/media-3261294%402x.png)

If [`ARSCNView`](arscnview.md) is your renderer, SceneKit applies camera grain to your app’s virtual content by default. For more information, see [`rendersCameraGrain`](arscnview/renderscameragrain.md).

##### Enable Image Noise on a Custom Renderer

For apps that display an AR experience using a custom Metal renderer, ARKit provides you with an [`cameraGrainTexture`](arframe/cameragraintexture.md) that matches the noise it detects in the current video stream. Set the noise texture onto your renderer to apply its characteristics to your virtual content.

The depth dimension of the image noise texture contains variations that you select at runtime based on the [`cameraGrainIntensity`](arframe/cameragrainintensity.md) of the current frame.

## See Also

- [var camera: ARCamera](arframe/camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var capturedImage: CVPixelBuffer](arframe/capturedimage.md)
  A pixel buffer containing the image captured by the camera.
- [var timestamp: TimeInterval](arframe/timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainIntensity: Float](arframe/cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var exifData: [String : Any]](arframe/exifdata.md)
  Auxiliary data for the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/cameragraintexture)*