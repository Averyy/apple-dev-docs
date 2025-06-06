# fields

**Framework**: PDFKit  
**Kind**: property

Returns an array of fields associated with the reset action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var fields: [String]? { get set }
```

#### Return Value

An array of `NSString` objects that corresponds to the `fieldNames` property of widget annotations (such as [`PDFAnnotationButtonWidget`](pdfannotationbuttonwidget.md)) on the PDF page. This method can return `NULL`.

## See Also

- [class PDFActionResetForm](pdfactionresetform.md)
  `PDFActionResetForm`, a subclass of `PDFAction`, defines methods for getting and clearing fields in a PDF form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfactionresetform/fields)*