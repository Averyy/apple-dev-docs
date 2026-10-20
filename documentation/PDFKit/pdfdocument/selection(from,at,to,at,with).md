# selection(from:at:to:at:with:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func selection(from startPage: PDFPage, at startPoint: CGPoint, to endPage: PDFPage, at endPoint: CGPoint, with granularity: PDFSelectionGranularity) -> PDFSelection?
```

*macOS*

```swift
func selection(from startPage: PDFPage, at startPoint: NSPoint, to endPage: PDFPage, at endPoint: NSPoint, with granularity: PDFSelectionGranularity) -> PDFSelection?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PDFSelection *) selectionFromPage:(PDFPage *) startPage atPoint:(CGPoint) startPoint toPage:(PDFPage *) endPage atPoint:(CGPoint) endPoint withGranularity:(PDFSelectionGranularity) granularity;
```

*macOS*

```objc
- (PDFSelection *) selectionFromPage:(PDFPage *) startPage atPoint:(NSPoint) startPoint toPage:(PDFPage *) endPage atPoint:(NSPoint) endPoint withGranularity:(PDFSelectionGranularity) granularity;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/selection(from:at:to:at:with:))*