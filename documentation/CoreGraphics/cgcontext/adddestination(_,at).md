# addDestination(_:at:)

**Framework**: Core Graphics  
**Kind**: method

Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.

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
func addDestination(_ name: CFString, at point: CGPoint)
```

## Parameters

- `name`: A destination name.
- `point`: A location in the current page of the PDF graphics context.

## See Also

- [func beginPDFPage(CFDictionary?)](cgcontext/beginpdfpage(_:).md)
  Begins a new page in a PDF graphics context.
- [func endPDFPage()](cgcontext/endpdfpage.md)
  Ends the current page in the PDF graphics context.
- [func setDestination(CFString, for: CGRect)](cgcontext/setdestination(_:for:).md)
  Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [func setURL(CFURL, for: CGRect)](cgcontext/seturl(_:for:).md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func addDocumentMetadata(CFData?)](cgcontext/adddocumentmetadata(_:).md)
  Associates custom metadata with the PDF document.
- [func closePDF()](cgcontext/closepdf.md)
  Closes a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/adddestination(_:at:))*