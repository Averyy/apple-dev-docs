# write(toFile:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Writes the document to a file at the specified path.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func write(toFile path: String) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path;
```

## See Also

### Related Documentation
- [func dataRepresentation() -> Data?](./datarepresentation%28%29.md)
  Returns a representation of the document as an `NSData` object.
### Writing Out the PDF Data
- [func write(toFile: String, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./write%28tofile,withoptions%29.md)
  Writes the document to a file at the specified path with the specified options.
- [func write(to: URL) -> Bool](./write%28to%29.md)
  Writes the document to a location specified by the passed-in URL.
- [func write(to: URL, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./write%28to,withoptions%29.md)
  Writes the document to the specified URL with the specified options.
- [Data Representations](../data-representations.md)
  Operations to represent PDF documents as data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/write(tofile:))*