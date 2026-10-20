# rVector

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The amount of red to multiply the source color values by.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var rVector: CIVector { get set }
```

```objc
@property (nonatomic, retain) CIVector * RVector;
```

## See Also

### Instance Properties
- [var aVector: CIVector](./avector.md)
  The amount of alpha to multiply the source color values by.
- [var bVector: CIVector](./bvector.md)
  The amount of blue to multiply the source color values by.
- [var gVector: CIVector](./gvector.md)
  The amount of green to multiply the source color values by.
- [var biasVector: CIVector](./biasvector.md)
  A vector that’s added to each color component.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormatrix/rvector)*