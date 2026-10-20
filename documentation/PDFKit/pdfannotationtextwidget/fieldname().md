# fieldName()

**Framework**: PDFKit  
**Kind**: method

Returns the internal name for the annotation text field.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func fieldName() -> String!
```

#### Return Value

The internal name for the annotation text field.

#### Discussion

Field names are optional, internal names that identify text fields in a PDF form. You use field names with the [`PDFActionResetForm`](pdfactionresetform.md) action.

Note that multiple `PDFAnnotationTextWidget` objects with the same field name always have the same text associated with that field name. When text is entered into one of the objects, the text associated with that field name is changed in all objects. If you need to ensure unique text for a `PDFAnnotationTextWidget` object, you must give it a unique field name (you can use [`setFieldName(_:)`](pdfannotationtextwidget/setfieldname(_:).md) to do this).

## See Also

- [class PDFAnnotationTextWidget](pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
- [func setFieldName(String!)](pdfannotationtextwidget/setfieldname(_:).md)
  Sets the internal field name for the annotation text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/fieldname())*