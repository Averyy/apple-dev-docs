# pdfContextBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bounds of the PDF context for the current page.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var pdfContextBounds: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect pdfContextBounds;
```

## Discussion

This value represents the bounds provided to the [`beginPage(withBounds:pageInfo:)`](./beginpage%28withbounds,pageinfo%29.md) method that created the current page. If the current page was created using the [`beginPage()`](./beginpage%28%29.md) method, the bounds are equal to those provided at the initialization of the PDF renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/pdfcontextbounds)*