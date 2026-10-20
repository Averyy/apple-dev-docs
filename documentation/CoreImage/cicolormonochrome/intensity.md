# intensity

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The intensity of the monochrome effect.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var intensity: Float { get set }
```

```objc
@property (nonatomic) float intensity;
```

#### Discussion

A value of 1.0 creates a monochrome image using the supplied color. A value of 0.0 has no effect on the image.

## See Also

### Instance Properties
- [var color: CIColor](./color.md)
  The monochrome color to apply to the image.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormonochrome/intensity)*