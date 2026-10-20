# footerHeight

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The height of the page footer.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var footerHeight: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat footerHeight;
```

#### Discussion

The footer is measured in points from the bottom of [`printableRect`](./printablerect.md) and is below the content area. The default footer height is 0.0

## See Also

### Specifying header and footer heights
- [var headerHeight: CGFloat](./headerheight.md)
  The height of the page header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/footerheight)*