# nrSharpness

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The amount of sharpening done when removing noise in the image before tracing the edges of the image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var nrSharpness: Float { get set }
```

```objc
@property (nonatomic) float NRSharpness;
```

#### Discussion

This improves the edge acquisition.

## See Also

### Instance Properties
- [var nrNoiseLevel: Float](./nrnoiselevel.md)
  The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [var contrast: Float](./contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var edgeIntensity: Float](./edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var threshold: Float](./threshold.md)
  A value that determines edge visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/nrsharpness)*