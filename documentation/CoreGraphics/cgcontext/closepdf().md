# closePDF()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Closes a PDF document.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func closePDF()
```

```c
extern void CGPDFContextClose(CGContextRef context);
```

#### Discussion

After closing the context, all pending data is written to the context destination, and the PDF file is completed. No additional data can be written to the destination context after the PDF document is closed.

## See Also

### Managing a PDF Graphics Context
- [func beginPDFPage(CFDictionary?)](./beginpdfpage%28_%29.md)
  Begins a new page in a PDF graphics context.
- [func endPDFPage()](./endpdfpage%28%29.md)
  Ends the current page in the PDF graphics context.
- [func addDestination(CFString, at: CGPoint)](./adddestination%28_,at%29.md)
  Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [func setDestination(CFString, for: CGRect)](./setdestination%28_,for%29.md)
  Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [func setURL(CFURL, for: CGRect)](./seturl%28_,for%29.md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func addDocumentMetadata(CFData?)](./adddocumentmetadata%28_%29.md)
  Associates custom metadata with the PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/closepdf())*