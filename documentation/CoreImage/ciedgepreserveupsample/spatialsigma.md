# spatialSigma

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A value that specifies the influence of the input image’s spatial information on the upsampling operation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var spatialSigma: Float { get set }
```

```objc
@property (nonatomic) float spatialSigma;
```

## See Also

### Instance Properties
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var lumaSigma: Float](./lumasigma.md)
  A value that specifies the influence of the input image’s luma information on the upsampling operation.
- [var smallImage: CIImage?](./smallimage.md)
  The image that the filter upsamples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciedgepreserveupsample/spatialsigma)*