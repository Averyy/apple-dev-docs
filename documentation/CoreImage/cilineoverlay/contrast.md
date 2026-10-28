# contrast

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The amount of antialiasing to use on the edges produced by this filter.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var contrast: Float { get set }
```

```objc
@property (nonatomic) float contrast;
```

## Discussion

Higher values produce higher contrast edges, that is, they’re less antialiased.

## See Also

### Instance Properties
- [var nrNoiseLevel: Float](./nrnoiselevel.md)
  The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [var nrSharpness: Float](./nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var edgeIntensity: Float](./edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var threshold: Float](./threshold.md)
  A value that determines edge visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/contrast)*