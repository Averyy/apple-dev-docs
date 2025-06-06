# setFieldName(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the internal field name associated with the widget annotation’s value.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setFieldName(_ name: String!)
```

#### Discussion

If the widget annotation is backed by PDF form data, it can associate an optional field name with a value or other data.

## Parameters

- `name`: The name to be used as the internal field name associated with the widget annotation.

## See Also

- [func fieldName() -> String!](pdfannotationchoicewidget/fieldname.md)
  Returns the internal field name associated with the widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/setfieldname(_:))*