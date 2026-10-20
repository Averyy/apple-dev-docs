# pageOrder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The print order for the pages of the operation.

**Availability**:
- macOS

## Declaration

```swift
var pageOrder: NSPrintOperation.PageOrder { get set }
```

```objc
@property NSPrintingPageOrder pageOrder;
```

## Parameters

- `order`: The print order. For a list of possible values, see [`NSPrintOperation.PageOrder`](./pageorder-swift.enum.md).

## See Also

### Managing Page Information
- [var currentPage: Int](./currentpage.md)
  The current page number being printed.
- [var pageRange: NSRange](./pagerange.md)
  The range of pages associated with the print operation.
- [NSPrintOperation.PageOrder](./pageorder-swift.enum.md)
  Constants that specify the page order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/pageorder-swift.property)*