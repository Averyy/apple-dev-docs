# maskImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A grayscale mask that defines the blend.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var maskImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * maskImage;
```

## Discussion

When a mask value is 0.0, the result is the background. When the mask value is 1.0, the result is the image.

## See Also

### Instance Properties
- [var backgroundImage: CIImage?](./backgroundimage.md)
  The image to use as a background image.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as a foreground image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendwithmask/maskimage)*