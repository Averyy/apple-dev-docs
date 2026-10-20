# lumaSigma

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A value that specifies the influence of the input image’s luma information on the upsampling operation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var lumaSigma: Float { get set }
```

```objc
@property (nonatomic) float lumaSigma;
```

## See Also

### Instance Properties
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var smallImage: CIImage?](./smallimage.md)
  The image that the filter upsamples.
- [var spatialSigma: Float](./spatialsigma.md)
  A value that specifies the influence of the input image’s spatial information on the upsampling operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciedgepreserveupsample/lumasigma)*