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
- [var paletteImage: CIImage?](./paletteimage.md)
  The input color palette, obtained by using a k-means clustering filter.
- [var perceptual: Bool](./perceptual.md)
  A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipalettecentroid/inputimage)*