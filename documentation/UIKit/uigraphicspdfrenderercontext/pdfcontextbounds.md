# pdfContextBounds

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

This value represents the bounds provided to the [`beginPage(withBounds:pageInfo:)`](uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:).md) method that created the current page. If the current page was created using the [`beginPage()`](uigraphicspdfrenderercontext/beginpage().md) method, the bounds are equal to those provided at the initialization of the PDF renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/pdfcontextbounds)*