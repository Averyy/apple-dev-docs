# nrNoiseLevel

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var nrNoiseLevel: Float { get set }
```

#### Discussion

Increasing the noise level helps to clean up the traced edges of the image.

## See Also

- [var nrSharpness: Float](cilineoverlay/nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var contrast: Float](cilineoverlay/contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var edgeIntensity: Float](cilineoverlay/edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var inputImage: CIImage?](cilineoverlay/inputimage.md)
  The image to use as an input image.
- [var threshold: Float](cilineoverlay/threshold.md)
  A value that determines edge visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/nrnoiselevel)*