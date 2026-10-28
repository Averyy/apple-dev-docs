# setOnStateValue(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the string that is associated with the on state of a radio button or checkbox control.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setOnStateValue(_ name: String!)
```

```objc
- (void) setOnStateValue:(NSString *) name;
```

## Discussion

Required for controls of types [`PDFAnnotationButtonWidget`](../pdfannotationbuttonwidget.md) and [`PDFAnnotationButtonWidget`](../pdfannotationbuttonwidget.md), the value of `name` describes the on state of the control (the off state is always labeled “Off”). Although “On” is an acceptable string for the on state of a single checkbox, a group of two or more radio buttons should have a unique string associated with each control.

For example, a form might display a group of 3 radio buttons that allow users to indicate an account type, such as savings, checking, or investment. The strings associated with the on states of these buttons could be “Savings,” “Checking,” and “Investment.” In this example, these 3 radio buttons also would share a field name string, such as “AccountType.”

## See Also

### Related Documentation
- [class PDFAnnotationButtonWidget](../pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
### Managing Control State Values and Form Fields
- [func onStateValue() -> String!](./onstatevalue%28%29.md)
  Returns the string associated with the on state of a radio button or checkbox control.
- [func fieldName() -> String!](./fieldname%28%29.md)
  Returns the internal name of a field (used for reset-form actions).
- [func setFieldName(String!)](./setfieldname%28_%29.md)
  Sets the internal name of a field (used for reset-form actions).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget/setonstatevalue(_:))*