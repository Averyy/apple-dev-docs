# paperRect

**Framework**: UIKit  
**Kind**: property

The size of the paper for printing.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var paperRect: CGRect { get }
```

#### Discussion

The value of this property is a rectangle that defines the size of paper chosen for the print job. The origin is always (0,0).

## See Also

- [var printPaper: UIPrintPaper?](uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var numberOfPages: Int](uiprintpagerenderer/numberofpages.md)
  The number of pages to render.
- [var printableRect: CGRect](uiprintpagerenderer/printablerect.md)
  The area in which printing can occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/paperrect)*