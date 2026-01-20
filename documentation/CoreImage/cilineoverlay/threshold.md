# threshold

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A value that determines edge visibility.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var threshold: Float { get set }
```

#### Discussion

Larger values thin out the edges.

## See Also

- [var nrNoiseLevel: Float](cilineoverlay/nrnoiselevel.md)
  The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [var nrSharpness: Float](cilineoverlay/nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var contrast: Float](cilineoverlay/contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var edgeIntensity: Float](cilineoverlay/edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var inputImage: CIImage?](cilineoverlay/inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/threshold)*