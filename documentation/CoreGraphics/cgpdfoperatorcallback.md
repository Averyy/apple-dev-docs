# CGPDFOperatorCallback

**Framework**: Core Graphics  
**Kind**: typealias

Performs custom processing for PDF operators.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CGPDFOperatorCallback = (CGPDFScannerRef, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Your callback function takes any action that’s appropriate for your application. For example, if you want to count the number of inline images in a PDF but ignore the image data, you would set a callback for the `EI` operator. In your callback you would increment a counter for each call.

## Parameters

- `scanner`: A CGPDFScanner object. Core Graphics passes the scanner to your callback function. The scanner contains the PDF content stream that has the PDF operator that corresponds to this callback.
- `info`: A pointer to data passed to the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatorcallback)*