# onStateValue()

**Framework**: PDFKit  
**Kind**: method

Returns the string associated with the on state of a radio button or checkbox control.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func onStateValue() -> String!
```

#### Return Value

The string associated with the on state of a radio button or checkbox control.

#### Discussion

This is a required string for controls of types [`PDFAnnotationButtonWidget`](pdfannotationbuttonwidget.md) and [`PDFAnnotationButtonWidget`](pdfannotationbuttonwidget.md). The off state is always labeled “Off”.

## See Also

- [class PDFAnnotationButtonWidget](pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
- [func setOnStateValue(String!)](pdfannotationbuttonwidget/setonstatevalue(_:).md)
  Sets the string that is associated with the on state of a radio button or checkbox control.
- [func fieldName() -> String!](pdfannotationbuttonwidget/fieldname.md)
  Returns the internal name of a field (used for reset-form actions).
- [func setFieldName(String!)](pdfannotationbuttonwidget/setfieldname(_:).md)
  Sets the internal name of a field (used for reset-form actions).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget/onstatevalue())*