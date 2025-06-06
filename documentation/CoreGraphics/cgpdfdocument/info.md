# info

**Framework**: Core Graphics  
**Kind**: property

Gets the information dictionary for a PDF document.

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
var info: CGPDFDictionaryRef? { get }
```

## See Also

- [var catalog: CGPDFDictionaryRef?](cgpdfdocument/catalog.md)
  Returns the document catalog of a Core Graphics PDF document.
- [var fileIdentifier: CGPDFArrayRef?](cgpdfdocument/fileidentifier.md)
  Gets the file identifier for a PDF document.
- [var numberOfPages: Int](cgpdfdocument/numberofpages.md)
  Returns the number of pages in a PDF document.
- [func getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)](cgpdfdocument/getversion(majorversion:minorversion:).md)
  Returns the major and minor version numbers of a Core Graphics PDF document.
- [func page(at: Int) -> CGPDFPage?](cgpdfdocument/page(at:).md)
  Returns a page from a Core Graphics PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/info)*