# write(to:)

**Framework**: PDFKit  
**Kind**: method

Writes the document to a location specified by the passed-in URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func write(to url: URL) -> Bool
```

## See Also

- [func dataRepresentation() -> Data?](pdfdocument/datarepresentation.md)
  Returns a representation of the document as an `NSData` object.
- [func write(toFile: String) -> Bool](pdfdocument/write(tofile:).md)
  Writes the document to a file at the specified path.
- [func write(toFile: String, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](pdfdocument/write(tofile:withoptions:).md)
  Writes the document to a file at the specified path with the specified options.
- [func write(to: URL, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](pdfdocument/write(to:withoptions:).md)
  Writes the document to the specified URL with the specified options.
- [Data Representations](data-representations.md)
  Operations to represent PDF documents as data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/write(to:))*