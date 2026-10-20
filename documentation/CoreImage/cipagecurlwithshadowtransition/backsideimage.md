# backsideImage

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The image that appears on the back of the source image as the page curls to reveal the target image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var backsideImage: CIImage? { get set }
```

```objc
@property (nonatomic, retain, nullable) CIImage * backsideImage;
```

## See Also

### Instance Properties
- [var angle: Float](./angle.md)
  The angle of the curling page.
- [var extent: CGRect](./extent.md)
  The extent of the effect.
- [var radius: Float](./radius.md)
  The radius of the curl.
- [var shadowAmount: Float](./shadowamount.md)
  The strength of the shadow.
- [var shadowExtent: CGRect](./shadowextent.md)
  The rectagular portion of input image that casts a shadow.
- [var shadowSize: Float](./shadowsize.md)
  The maximum size, in pixels, of the shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipagecurlwithshadowtransition/backsideimage)*