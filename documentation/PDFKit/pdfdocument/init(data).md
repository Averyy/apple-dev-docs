# init(data:)

**Framework**: PDFKit  
**Kind**: init  
**Role**: Initializer

Initializes a `PDFDocument` object with the passed-in data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(data: Data)
```

```objc
- (instancetype) initWithData:(NSData *) data;
```

#### Return Value

A `PDFDocument` instance initialized with the passed-in PDF data, or `NULL` if the object could not be initialized.

#### Discussion

The data must be PDF data encapsulated in an `NSData` object; otherwise this method returns `NULL`.

## See Also

### Initializing Documents
- [init?(url: URL)](./init%28url%29-98jte.md)
  Initializes a `PDFDocument` object with the contents at the specified URL (if the URL is invalid, this method returns `NULL`).
- [init()](./init%28%29.md)
  Initializes a `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/init(data:))*