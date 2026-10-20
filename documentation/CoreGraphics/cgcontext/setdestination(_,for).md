# setDestination(_:for:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets a destination to jump to when a rectangle in the current PDF page is clicked.

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
func setDestination(_ name: CFString, for rect: CGRect)
```

```c
extern void CGPDFContextSetDestinationForRect(CGContextRef context, CFStringRef name, CGRect rect);
```

## Parameters

- `name`: A destination name.
- `rect`: A rectangle that specifies an area of the current page of a PDF graphics context. The rectangle is specified in default user space (not device space).

## See Also

### Managing a PDF Graphics Context
- [func beginPDFPage(CFDictionary?)](./beginpdfpage%28_%29.md)
  Begins a new page in a PDF graphics context.
- [func endPDFPage()](./endpdfpage%28%29.md)
  Ends the current page in the PDF graphics context.
- [func addDestination(CFString, at: CGPoint)](./adddestination%28_,at%29.md)
  Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.
- [func setURL(CFURL, for: CGRect)](./seturl%28_,for%29.md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func addDocumentMetadata(CFData?)](./adddocumentmetadata%28_%29.md)
  Associates custom metadata with the PDF document.
- [func closePDF()](./closepdf%28%29.md)
  Closes a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setdestination(_:for:))*