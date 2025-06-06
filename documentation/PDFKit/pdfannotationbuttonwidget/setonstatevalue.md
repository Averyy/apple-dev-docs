# setOnStateValue(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the string that is associated with the on state of a radio button or checkbox control.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setOnStateValue(_ name: String!)
```

#### Discussion

Required for controls of types [`PDFAnnotationButtonWidget`](pdfannotationbuttonwidget.md) and [`PDFAnnotationButtonWidget`](pdfannotationbuttonwidget.md), the value of `name` describes the on state of the control (the off state is always labeled “Off”). Although “On” is an acceptable string for the on state of a single checkbox, a group of two or more radio buttons should have a unique string associated with each control.

For example, a form might display a group of 3 radio buttons that allow users to indicate an account type, such as savings, checking, or investment. The strings associated with the on states of these buttons could be “Savings,” “Checking,” and “Investment.” In this example, these 3 radio buttons also would share a field name string, such as “AccountType.”

## See Also

- [class PDFAnnotationButtonWidget](pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
- [func onStateValue() -> String!](pdfannotationbuttonwidget/onstatevalue.md)
  Returns the string associated with the on state of a radio button or checkbox control.
- [func fieldName() -> String!](pdfannotationbuttonwidget/fieldname.md)
  Returns the internal name of a field (used for reset-form actions).
- [func setFieldName(String!)](pdfannotationbuttonwidget/setfieldname(_:).md)
  Sets the internal name of a field (used for reset-form actions).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget/setonstatevalue(_:))*