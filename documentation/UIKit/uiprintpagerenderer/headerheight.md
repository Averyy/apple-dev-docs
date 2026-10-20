# headerHeight

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The height of the page header.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var headerHeight: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat headerHeight;
```

#### Discussion

The header is measured in points from the top of [`printableRect`](./printablerect.md) and is above the content area. The default header height is 0.0.

## See Also

### Specifying header and footer heights
- [var footerHeight: CGFloat](./footerheight.md)
  The height of the page footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/headerheight)*