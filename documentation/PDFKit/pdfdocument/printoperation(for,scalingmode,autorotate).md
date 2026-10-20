# printOperation(for:scalingMode:autoRotate:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns a print operation suitable for printing the PDF document.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func printOperation(for printInfo: NSPrintInfo?, scalingMode scaleMode: PDFPrintScalingMode, autoRotate doRotate: Bool) -> NSPrintOperation?
```

```objc
- (NSPrintOperation *) printOperationForPrintInfo:(NSPrintInfo *) printInfo scalingMode:(PDFPrintScalingMode) scaleMode autoRotate:(BOOL) doRotate;
```

## See Also

### Printing Documents for macOS
- [enum PDFPrintScalingMode](../pdfprintscalingmode.md)
  The type of scaling to be used when printing a page (see [`PDFDocument`](../pdfdocument.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/printoperation(for:scalingmode:autorotate:))*