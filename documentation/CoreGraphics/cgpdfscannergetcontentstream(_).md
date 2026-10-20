# CGPDFScannerGetContentStream(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the content stream associated with a PDF scanner object.

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
func CGPDFScannerGetContentStream(_ scanner: CGPDFScannerRef) -> CGPDFContentStreamRef
```

```c
extern CGPDFContentStreamRefCGPDFScannerGetContentStream(CGPDFScannerRef scanner);
```

#### Return Value

The content stream associated with `scanner`.

## Parameters

- `scanner`: The scanner object whose content stream you want to obtain.

## See Also

### Parsing Content
- [func CGPDFScannerScan(CGPDFScannerRef) -> Bool](./cgpdfscannerscan%28_%29.md)
  Parses the content stream of a PDF scanner object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannergetcontentstream(_:))*