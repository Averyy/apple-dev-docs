# addDestination(_:at:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets a destination to jump to when a point in the current page of a PDF graphics context is clicked.

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
func addDestination(_ name: CFString, at point: CGPoint)
```

```c
extern void CGPDFContextAddDestinationAtPoint(CGContextRef context, CFStringRef name, CGPoint point);
```

## Parameters

- `name`: A destination name.
- `point`: A location in the current page of the PDF graphics context.

## See Also

### Managing a PDF Graphics Context
- [func beginPDFPage(CFDictionary?)](./beginpdfpage%28_%29.md)
  Begins a new page in a PDF graphics context.
- [func endPDFPage()](./endpdfpage%28%29.md)
  Ends the current page in the PDF graphics context.
- [func setDestination(CFString, for: CGRect)](./setdestination%28_,for%29.md)
  Sets a destination to jump to when a rectangle in the current PDF page is clicked.
- [func setURL(CFURL, for: CGRect)](./seturl%28_,for%29.md)
  Sets the URL associated with a rectangle in a PDF graphics context.
- [func addDocumentMetadata(CFData?)](./adddocumentmetadata%28_%29.md)
  Associates custom metadata with the PDF document.
- [func closePDF()](./closepdf%28%29.md)
  Closes a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/adddestination(_:at:))*