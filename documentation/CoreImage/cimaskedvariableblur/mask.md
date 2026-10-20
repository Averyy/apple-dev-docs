# mask

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A grayscale mask that defines the blur amount.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var mask: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * mask;
```

## See Also

### Instance Properties
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var radius: Float](./radius.md)
  The distance from the center of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimaskedvariableblur/mask)*