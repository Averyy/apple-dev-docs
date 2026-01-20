# shadingImage

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The image to use as the height field.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var shadingImage: CIImage? { get set }
```

#### Discussion

The resulting image has greater heights with lighter shades, and lesser heights (lower areas) with darker shades.

## See Also

- [var inputImage: CIImage?](cishadedmaterial/inputimage.md)
  The image to use as an input image.
- [var scale: Float](cishadedmaterial/scale.md)
  The scale of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cishadedmaterial/shadingimage)*