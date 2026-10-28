# printFormattersForPage(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the print formatters for a specified page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func printFormattersForPage(at pageIndex: Int) -> [UIPrintFormatter]?
```

```objc
- (NSArray<UIPrintFormatter *> *) printFormattersForPageAtIndex:(NSInteger) pageIndex;
```

## Return Value

An array of [`UIPrintFormatter`](../uiprintformatter.md) objects. A print formatter can be an instance of [`UISimpleTextPrintFormatter`](../uisimpletextprintformatter.md), [`UIMarkupTextPrintFormatter`](../uimarkuptextprintformatter.md), or [`UIViewPrintFormatter`](../uiviewprintformatter.md).

## Discussion

A print formatter is associated with a starting page of printable content through the [`addPrintFormatter(_:startingAtPageAt:)`](./addprintformatter%28_,startingatpageat%29.md) method or the [`startPage`](../uiprintformatter/startpage.md) property of [`UIPrintFormatter`](../uiprintformatter.md). The number of pages from that page is determined by the [`pageCount`](../uiprintformatter/pagecount.md) property, which [`UIPrintFormatter`](../uiprintformatter.md) computes based on layout metrics and content.

## Parameters

- `pageIndex`: The index of a page of printable content.

## See Also

### Managing print formatters
- [func addPrintFormatter(UIPrintFormatter, startingAtPageAt: Int)](./addprintformatter%28_,startingatpageat%29.md)
  Adds a print formatter to the page renderer starting at the specified page.
- [var printFormatters: [UIPrintFormatter]?](./printformatters.md)
  The print formatters for the page renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printformattersforpage(at:))*