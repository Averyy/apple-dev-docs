# capturedImage

**Framework**: ARKit  
**Kind**: property

A pixel buffer containing the image captured by the camera.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var capturedImage: CVPixelBuffer { get }
```

## Mentions

- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)

#### Discussion

ARKit captures pixel buffers in a full-range planar YCbCr format (also known as YUV) format according to the ITU R. 601-4 standard. (You can verify this by checking the [`kCVImageBufferYCbCrMatrixKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferYCbCrMatrixKey) pixel buffer attachment.)

Unlike some uses of that standard, ARKit captures full-range color space values, not video-range values. To correctly render these images on a device display, you’ll need to access the luma and chroma planes of the pixel buffer and convert full-range YCbCr values to an sRGB (or ITU R. 709) format according to the ITU-T T.871 specification.

The following matrix (shown in Metal shader syntax) performs this conversion when multiplied by a 4-element vector (containing Y’, Cb, Cr values and an “alpha” value of 1.0):

```cpp
const float4x4 ycbcrToRGBTransform = float4x4(
    float4(+1.0000f, +1.0000f, +1.0000f, +0.0000f),
    float4(+0.0000f, -0.3441f, +1.7720f, +0.0000f),
    float4(+1.4020f, -0.7141f, +0.0000f, +0.0000f),
    float4(-0.7010f, +0.5291f, -0.8860f, +1.0000f)
);
```

For more details, see [`Displaying an AR Experience with Metal`](displaying-an-ar-experience-with-metal.md), or use the Metal variant of the AR app template when creating a new project in Xcode.

## See Also

- [var camera: ARCamera](arframe/camera.md)
  Information about the camera position, orientation, and imaging parameters used to capture the frame.
- [var timestamp: TimeInterval](arframe/timestamp.md)
  The time at which the frame was captured.
- [var cameraGrainIntensity: Float](arframe/cameragrainintensity.md)
  A value that specifies the amount of grain present in the camera grain texture.
- [var cameraGrainTexture: (any MTLTexture)?](arframe/cameragraintexture.md)
  A tileable Metal texture created by ARKit to match the visual characteristics of the current video stream.
- [var exifData: [String : Any]](arframe/exifdata.md)
  Auxiliary data for the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/capturedimage)*