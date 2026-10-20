# shadingImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An image that looks like a shaded sphere enclosed in a square.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shadingImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * shadingImage;
```

## See Also

### Instance Properties
- [var angle: Float](./angle.md)
  The angle of the curling page.
- [var backsideImage: CIImage?](./backsideimage.md)
  The image that appears on the back of the source image as the page curls to reveal the target image.
- [var extent: CGRect](./extent.md)
  The extent of the effect.
- [var radius: Float](./radius.md)
  The radius of the curl.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipagecurltransition/shadingimage)*