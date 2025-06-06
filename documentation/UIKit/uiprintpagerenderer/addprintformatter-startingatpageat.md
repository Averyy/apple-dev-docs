# addPrintFormatter(_:startingAtPageAt:)

**Framework**: UIKit  
**Kind**: method

Adds a print formatter to the page renderer starting at the specified page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addPrintFormatter(_ formatter: UIPrintFormatter, startingAtPageAt pageIndex: Int)
```

#### Discussion

You can dissociate a print formatter from its page renderer by calling the [`removeFromPrintPageRenderer()`](uiprintformatter/removefromprintpagerenderer().md) method on the print formatter.

## Parameters

- `formatter`: The   object to add to the page renderer. A print formatter can be an instance of  ,  , or  .
- `pageIndex`: The index identifying the first page with which the print formatter should be associated with. This value overrides the   property of the print formatter.

## See Also

- [func printFormattersForPage(at: Int) -> [UIPrintFormatter]?](uiprintpagerenderer/printformattersforpage(at:).md)
  Returns the print formatters for a specified page.
- [var printFormatters: [UIPrintFormatter]?](uiprintpagerenderer/printformatters.md)
  The print formatters for the page renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/addprintformatter(_:startingatpageat:))*