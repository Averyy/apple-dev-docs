# endPDFPage()

**Framework**: Core Graphics  
**Kind**: method

Ends the current page in the PDF graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func endPDFPage()
```

#### Discussion

You can call [`endPDFPage()`](cgcontext/endpdfpage().md) only after you call the function [`beginPDFPage(_:)`](cgcontext/beginpdfpage(_:).md).

## See Also

- [func beginPDFPage(CFDictionary?)](cgcontext/beginpdfpage(_:).md)
  Begins a new page in a PDF graphics context.
- [func addDestination(CFString, at: CGPoint)](cgcontext/adddestination(_:at:).md)
  Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [func setDestination(CFString, for: CGRect)](cgcontext/setdestination(_:for:).md)
  Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [func setURL(CFURL, for: CGRect)](cgcontext/seturl(_:for:).md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func addDocumentMetadata(CFData?)](cgcontext/adddocumentmetadata(_:).md)
  Associates custom metadata with the PDF document.
- [func closePDF()](cgcontext/closepdf.md)
  Closes a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/endpdfpage())*