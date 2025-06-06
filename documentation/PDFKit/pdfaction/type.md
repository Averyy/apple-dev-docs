# type

**Framework**: PDFKit  
**Kind**: property

Returns the type of the action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var type: String { get }
```

#### Return Value

The type of the PDF action.

#### Discussion

The PDF action type returned by this method may not correspond precisely to the name of a `PDFAction` subclass. For example, a `PDFActionURL` object might return “URI” or “Launch,” depending on the original action as defined by the Adobe PDF Specification. In the PDF Kit, these two actions are handled in the single `PDFActionURL` subclass, and the more familiar term “URL” is used instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfaction/type)*