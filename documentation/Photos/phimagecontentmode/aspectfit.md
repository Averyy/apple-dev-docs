# PHImageContentMode.aspectFit

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Scales the image so that its larger dimension fits the target size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case aspectFit
```

```c
PHImageContentModeAspectFit
```

#### Discussion

Use this option when you want the entire image to be visible, such as when presenting it in a view with the [`UIView.ContentMode.scaleAspectFit`](../../UIKit/uiview/contentmode-swift.enum/scaleaspectfit.md) content mode.

## See Also

### Constants
- [static var `default`: PHImageContentMode](./default.md)
  Fits the image to the requested size using the default option, [`PHImageContentMode.aspectFit`](./aspectfit.md).
- [PHImageContentMode.aspectFill](./aspectfill.md)
  Scales the image so that it completely fills the target size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagecontentmode/aspectfit)*