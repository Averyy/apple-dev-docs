# printFormatters

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The print formatters for the page renderer.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printFormatters: [UIPrintFormatter]? { get set }
```

```objc
@property (atomic, copy, nullable) NSArray<UIPrintFormatter *> * printFormatters;
```

## Discussion

The elements of the array are [`UIPrintFormatter`](../uiprintformatter.md) objects. A print formatter can be an instance of [`UISimpleTextPrintFormatter`](../uisimpletextprintformatter.md), [`UIMarkupTextPrintFormatter`](../uimarkuptextprintformatter.md), or [`UIViewPrintFormatter`](../uiviewprintformatter.md). Print formatters added this way to a page renderer are associated with page ranges through each print formatter’s [`startPage`](../uiprintformatter/startpage.md) and [`pageCount`](../uiprintformatter/pagecount.md) properties.

## See Also

### Managing print formatters
- [func addPrintFormatter(UIPrintFormatter, startingAtPageAt: Int)](./addprintformatter%28_,startingatpageat%29.md)
  Adds a print formatter to the page renderer starting at the specified page.
- [func printFormattersForPage(at: Int) -> [UIPrintFormatter]?](./printformattersforpage%28at%29.md)
  Returns the print formatters for a specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printformatters)*