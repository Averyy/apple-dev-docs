# addDocumentMetadata(_:)

**Framework**: Core Graphics  
**Kind**: method

Associates custom metadata with the PDF document.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addDocumentMetadata(_ metadata: CFData?)
```

## Parameters

- `metadata`: A stream of XML data that is formatted according to the Extensible Metadata Platform, as described in section 10.2.2., “Metadata Streams”, of the PDF 1.7 specification.

## See Also

- [func beginPDFPage(CFDictionary?)](cgcontext/beginpdfpage(_:).md)
  Begins a new page in a PDF graphics context.
- [func endPDFPage()](cgcontext/endpdfpage.md)
  Ends the current page in the PDF graphics context.
- [func addDestination(CFString, at: CGPoint)](cgcontext/adddestination(_:at:).md)
  Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [func setDestination(CFString, for: CGRect)](cgcontext/setdestination(_:for:).md)
  Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [func setURL(CFURL, for: CGRect)](cgcontext/seturl(_:for:).md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func closePDF()](cgcontext/closepdf.md)
  Closes a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/adddocumentmetadata(_:))*