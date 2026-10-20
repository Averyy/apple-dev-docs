# setURL(_:for:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the URL associated with a rectangle in a PDF graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setURL(_ url: CFURL, for rect: CGRect)
```

```c
extern void CGPDFContextSetURLForRect(CGContextRef context, CFURLRef url, CGRect rect);
```

## Parameters

- `url`: A URL that specifies the destination of the contents associated with the rectangle.
- `rect`: A rectangle specified in default user space (not device space).

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
- [func addDocumentMetadata(CFData?)](./adddocumentmetadata%28_%29.md)
  Associates custom metadata with the PDF document.
- [func closePDF()](./closepdf%28%29.md)
  Closes a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/seturl(_:for:))*