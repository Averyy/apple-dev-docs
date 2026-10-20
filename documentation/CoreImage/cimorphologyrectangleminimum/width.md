# width

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The width, in pixels, of the morphological structuring element.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var width: Float { get set }
```

```objc
@property (nonatomic) float width;
```

#### Discussion

The value is rounded to the nearest odd integer.

## See Also

### Instance Properties
- [var height: Float](./height.md)
  The height, in pixels, of the morphological structuring element.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimorphologyrectangleminimum/width)*