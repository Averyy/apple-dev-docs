# printableRect

**Framework**: UIKit  
**Kind**: property

The area in which printing can occur.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printableRect: CGRect { get }
```

#### Discussion

The value of this property is a rectangle that defines the area in which the printer can print content. Sometimes this is referred to as the imageable area of the paper.

## See Also

- [var printPaper: UIPrintPaper?](uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var numberOfPages: Int](uiprintpagerenderer/numberofpages.md)
  The number of pages to render.
- [var paperRect: CGRect](uiprintpagerenderer/paperrect.md)
  The size of the paper for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printablerect)*