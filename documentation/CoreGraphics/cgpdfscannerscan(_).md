# CGPDFScannerScan(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Parses the content stream of a PDF scanner object.

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
func CGPDFScannerScan(_ scanner: CGPDFScannerRef) -> Bool
```

```c
extern bool CGPDFScannerScan(CGPDFScannerRef scanner);
```

#### Return Value

[`true`](../Swift/true.md) if the entire stream is parsed successfully; [`false`](../Swift/false.md) if parsing fails (for example, if the stream data is corrupted).

#### Discussion

The function [`CGPDFScannerScan(_:)`](./cgpdfscannerscan%28_%29.md) parses the PDF content stream associated with the scanner. Each time Core Graphics parses a PDF operator for which you register a callback, Core Graphics invokes your callback.

## Parameters

- `scanner`: The scanner object whose content stream you want to parse.

## See Also

### Parsing Content
- [func CGPDFScannerGetContentStream(CGPDFScannerRef) -> CGPDFContentStreamRef](./cgpdfscannergetcontentstream%28_%29.md)
  Returns the content stream associated with a PDF scanner object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerscan(_:))*