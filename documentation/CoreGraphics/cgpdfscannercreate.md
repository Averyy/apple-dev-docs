# CGPDFScannerCreate(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Creates a PDF scanner.

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
func CGPDFScannerCreate(_ cs: CGPDFContentStreamRef, _ table: CGPDFOperatorTableRef?, _ info: UnsafeMutableRawPointer?) -> CGPDFScannerRef
```

#### Return Value

A PDF scanner object. In Objective-C, you’re responsible for releasing this object by calling the function [`CGPDFScannerRelease(_:)`](cgpdfscannerrelease(_:).md).

#### Discussion

When you want to parse the contents of the PDF stream, call the function [`CGPDFScannerScan(_:)`](cgpdfscannerscan(_:).md).

## Parameters

- `cs`: A PDF content stream object. (See  .)
- `table`: A table of callbacks for the PDF operators you want to handle.
- `info`: A pointer to data you want passed to your callback function. (See  .)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannercreate(_:_:_:))*