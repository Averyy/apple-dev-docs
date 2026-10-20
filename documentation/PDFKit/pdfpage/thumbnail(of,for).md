# thumbnail(of:for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func thumbnail(of size: CGSize, for box: PDFDisplayBox) -> UIImage
```

*macOS*

```swift
func thumbnail(of size: NSSize, for box: PDFDisplayBox) -> NSImage
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (UIImage *) thumbnailOfSize:(CGSize) size forBox:(PDFDisplayBox) box;
```

*macOS*

```objc
- (NSImage *) thumbnailOfSize:(NSSize) size forBox:(PDFDisplayBox) box;
```

## See Also

### Instance Methods
- [func draw(with: PDFDisplayBox, to: CGContext)](./draw%28with,to%29.md)
- [func transform(CGContext, for: PDFDisplayBox)](./transform%28_,for%29.md)
- [func transform(for: PDFDisplayBox) -> CGAffineTransform](./transform%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/thumbnail(of:for:))*