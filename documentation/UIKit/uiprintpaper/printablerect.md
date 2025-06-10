# printableRect

**Framework**: UIKit  
**Kind**: property

The rectangle that represents the portion of the paper that can be imaged upon.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printableRect: CGRect { get }
```

#### Discussion

Typically, UIKit passes this value into the last argument of the [`UIPrintPageRenderer`](uiprintpagerenderer.md) method [`drawPage(at:in:)`](uiprintpagerenderer/drawpage(at:in:).md).

## See Also

- [var paperSize: CGSize](uiprintpaper/papersize.md)
  The size of the sheet to use for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpaper/printablerect)*