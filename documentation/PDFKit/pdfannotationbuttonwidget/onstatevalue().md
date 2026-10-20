# onStateValue()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the string associated with the on state of a radio button or checkbox control.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func onStateValue() -> String!
```

```objc
- (NSString *) onStateValue;
```

#### Return Value

The string associated with the on state of a radio button or checkbox control.

#### Discussion

This is a required string for controls of types [`PDFAnnotationButtonWidget`](../pdfannotationbuttonwidget.md) and [`PDFAnnotationButtonWidget`](../pdfannotationbuttonwidget.md). The off state is always labeled “Off”.

## See Also

### Related Documentation
- [class PDFAnnotationButtonWidget](../pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
### Managing Control State Values and Form Fields
- [func setOnStateValue(String!)](./setonstatevalue%28_%29.md)
  Sets the string that is associated with the on state of a radio button or checkbox control.
- [func fieldName() -> String!](./fieldname%28%29.md)
  Returns the internal name of a field (used for reset-form actions).
- [func setFieldName(String!)](./setfieldname%28_%29.md)
  Sets the internal name of a field (used for reset-form actions).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget/onstatevalue())*