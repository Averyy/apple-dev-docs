# scale

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The scaling factor to use on the image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var scale: Float { get set }
```

```objc
@property (nonatomic) float scale;
```

#### Discussion

Values less than 1.0 scale down the images. Values greater than 1.0 scale up the image.

## See Also

### Instance Properties
- [var aspectRatio: Float](./aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilanczosscaletransform/scale)*