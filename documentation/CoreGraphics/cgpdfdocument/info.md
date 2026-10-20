# info

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Gets the information dictionary for a PDF document.

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
var info: CGPDFDictionaryRef? { get }
```

```c
extern CGPDFDictionaryRefCGPDFDocumentGetInfo(CGPDFDocumentRef document);
```

## See Also

### Examining a PDF Document
- [var catalog: CGPDFDictionaryRef?](./catalog.md)
  Returns the document catalog of a Core Graphics PDF document.
- [var fileIdentifier: CGPDFArrayRef?](./fileidentifier.md)
  Gets the file identifier for a PDF document.
- [var numberOfPages: Int](./numberofpages.md)
  Returns the number of pages in a PDF document.
- [func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)](./getversion%28majorversion,minorversion%29.md)
  Returns the major and minor version numbers of a Core Graphics PDF document.
- [func page(at: Int) -> CGPDFPage?](./page%28at%29.md)
  Returns a page from a Core Graphics PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/info)*