# dataRepresentation()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSData *) dataRepresentation;
```

## See Also

### Related Documentation
- [func write(toFile: String) -> Bool](./write%28tofile%29.md)
  Writes the document to a file at the specified path.
- [func write(to: URL) -> Bool](./write%28to%29.md)
  Writes the document to a location specified by the passed-in URL.
### Creating Data Representations
- [func dataRepresentation(options: [AnyHashable : Any]) -> Data?](./datarepresentation%28options%29.md)
  Returns a representation of the document as an `NSData` object with additional options applied, such as filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/datarepresentation())*