# dataRepresentation(options:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns a representation of the document as an `NSData` object with additional options applied, such as filters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dataRepresentation(options: [AnyHashable : Any] = [:]) -> Data?
```

```objc
- (NSData *) dataRepresentationWithOptions:(NSDictionary *) options;
```

## See Also

### Creating Data Representations
- [func dataRepresentation() -> Data?](./datarepresentation%28%29.md)
  Returns a representation of the document as an `NSData` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/datarepresentation(options:))*