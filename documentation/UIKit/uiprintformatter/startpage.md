# startPage

**Framework**: UIKit  
**Kind**: property

The index of the first page that the print formatter lays out.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var startPage: Int { get set }
```

#### Discussion

The value is a zero-based index. You can set the starting page of a print formatter by assigning an index to this property or by passing one as the second argument of the [`addPrintFormatter(_:startingAtPageAt:)`](uiprintpagerenderer/addprintformatter(_:startingatpageat:).md) method of [`UIPrintPageRenderer`](uiprintpagerenderer.md).

## See Also

- [var pageCount: Int](uiprintformatter/pagecount.md)
  The number of pages to print.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/startpage)*