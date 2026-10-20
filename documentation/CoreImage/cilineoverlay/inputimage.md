# inputImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The image to use as an input image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * inputImage;
```

## See Also

### Instance Properties
- [var nrNoiseLevel: Float](./nrnoiselevel.md)
  The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [var nrSharpness: Float](./nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var contrast: Float](./contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var edgeIntensity: Float](./edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var threshold: Float](./threshold.md)
  A value that determines edge visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay/inputimage)*