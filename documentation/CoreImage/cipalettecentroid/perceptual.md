# perceptual

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var perceptual: Bool { get set }
```

```objc
@property (nonatomic) bool perceptual;
```

## See Also

### Instance Properties
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var paletteImage: CIImage?](./paletteimage.md)
  The input color palette, obtained by using a k-means clustering filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipalettecentroid/perceptual)*