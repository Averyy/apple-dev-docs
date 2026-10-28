# init(url:)

**Framework**: PDFKit  
**Kind**: init  
**Role**: Initializer

Initializes a `PDFDocument` object with the contents at the specified URL (if the URL is invalid, this method returns `NULL`).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

## Return Value

A `PDFDocument` instance initialized with the data at the passed-in URL or `NULL` if the object could not be initialized or if the URL is invalid.

## See Also

### Initializing Documents
- [init?(data: Data)](./init%28data%29.md)
  Initializes a `PDFDocument` object with the passed-in data.
- [init()](./init%28%29.md)
  Initializes a `PDFDocument` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/init(url:)-98jte)*