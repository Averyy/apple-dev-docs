# catalog

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the document catalog of a Core Graphics PDF document.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var catalog: CGPDFDictionaryRef? { get }
```

```c
extern CGPDFDictionaryRefCGPDFDocumentGetCatalog(CGPDFDocumentRef document);
```

## Discussion

The entries in a PDF document catalog recursively describe the contents of the PDF document. You can access the contents of a PDF document catalog by calling the function [`catalog`](./catalog.md). For information on accessing PDF metadata, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## See Also

### Examining a PDF Document
- [var fileIdentifier: CGPDFArrayRef?](./fileidentifier.md)
  Gets the file identifier for a PDF document.
- [var info: CGPDFDictionaryRef?](./info.md)
  Gets the information dictionary for a PDF document.
- [var numberOfPages: Int](./numberofpages.md)
  Returns the number of pages in a PDF document.
- [func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)](./getversion%28majorversion,minorversion%29.md)
  Returns the major and minor version numbers of a Core Graphics PDF document.
- [func page(at: Int) -> CGPDFPage?](./page%28at%29.md)
  Returns a page from a Core Graphics PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/catalog)*