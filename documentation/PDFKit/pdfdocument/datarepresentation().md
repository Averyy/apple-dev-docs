# dataRepresentation()

**Framework**: PDFKit  
**Kind**: method

Returns a representation of the document as an `NSData` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dataRepresentation() -> Data?
```

## See Also

- [func write(toFile: String) -> Bool](pdfdocument/write(tofile:).md)
  Writes the document to a file at the specified path.
- [func write(to: URL) -> Bool](pdfdocument/write(to:).md)
  Writes the document to a location specified by the passed-in URL.
- [func dataRepresentation(options: [AnyHashable : Any]) -> Data?](pdfdocument/datarepresentation(options:).md)
  Returns a representation of the document as an `NSData` object with additional options applied, such as filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/datarepresentation())*