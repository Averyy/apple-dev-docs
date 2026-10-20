# fieldName()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the internal name for the annotation text field.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func fieldName() -> String!
```

```objc
- (NSString *) fieldName;
```

#### Return Value

The internal name for the annotation text field.

#### Discussion

Field names are optional, internal names that identify text fields in a PDF form. You use field names with the [`PDFActionResetForm`](../pdfactionresetform.md) action.

Note that multiple `PDFAnnotationTextWidget` objects with the same field name always have the same text associated with that field name. When text is entered into one of the objects, the text associated with that field name is changed in all objects. If you need to ensure unique text for a `PDFAnnotationTextWidget` object, you must give it a unique field name (you can use [`setFieldName(_:)`](./setfieldname%28_%29.md) to do this).

## See Also

### Related Documentation
- [class PDFAnnotationTextWidget](../pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
### Working with Field Names
- [func setFieldName(String!)](./setfieldname%28_%29.md)
  Sets the internal field name for the annotation text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/fieldname())*