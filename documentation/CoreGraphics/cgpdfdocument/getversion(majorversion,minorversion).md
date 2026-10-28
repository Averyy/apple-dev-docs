# getVersion(majorVersion:minorVersion:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Returns the major and minor version numbers of a Core Graphics PDF document.

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
func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)
```

```c
extern void CGPDFDocumentGetVersion(CGPDFDocumentRef document, int *majorVersion, int *minorVersion);
```

## Discussion

On return, the values of the `majorVersion` and `minorVersion` parameters are set to the major and minor version numbers of the document respectively.

## Parameters

- `majorVersion`: On return, contains the major version number of the document.
- `minorVersion`: On return, contains the minor version number of the document.

## See Also

### Examining a PDF Document
- [var catalog: CGPDFDictionaryRef?](./catalog.md)
  Returns the document catalog of a Core Graphics PDF document.
- [var fileIdentifier: CGPDFArrayRef?](./fileidentifier.md)
  Gets the file identifier for a PDF document.
- [var info: CGPDFDictionaryRef?](./info.md)
  Gets the information dictionary for a PDF document.
- [var numberOfPages: Int](./numberofpages.md)
  Returns the number of pages in a PDF document.
- [func page(at: Int) -> CGPDFPage?](./page%28at%29.md)
  Returns a page from a Core Graphics PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/getversion(majorversion:minorversion:))*