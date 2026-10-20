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
- [var lumaSigma: Float](./lumasigma.md)
  A value that specifies the influence of the input image’s luma information on the upsampling operation.
- [var smallImage: CIImage?](./smallimage.md)
  The image that the filter upsamples.
- [var spatialSigma: Float](./spatialsigma.md)
  A value that specifies the influence of the input image’s spatial information on the upsampling operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciedgepreserveupsample/inputimage)*