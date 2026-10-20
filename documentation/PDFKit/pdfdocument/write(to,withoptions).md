# write(to:withOptions:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Writes the document to the specified URL with the specified options.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func write(to url: URL, withOptions options: [PDFDocumentWriteOption : Any]? = nil) -> Bool
```

```objc
- (BOOL) writeToURL:(NSURL *) url withOptions:(NSDictionary<NSString *,id> *) options;
```

## See Also

### Related Documentation
- [func dataRepresentation() -> Data?](./datarepresentation%28%29.md)
  Returns a representation of the document as an `NSData` object.
### Writing Out the PDF Data
- [func write(toFile: String) -> Bool](./write%28tofile%29.md)
  Writes the document to a file at the specified path.
- [func write(toFile: String, withOptions: [PDFDocumentWriteOption : Any]?) -> Bool](./write%28tofile,withoptions%29.md)
  Writes the document to a file at the specified path with the specified options.
- [func write(to: URL) -> Bool](./write%28to%29.md)
  Writes the document to a location specified by the passed-in URL.
- [Data Representations](../data-representations.md)
  Operations to represent PDF documents as data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/write(to:withoptions:))*