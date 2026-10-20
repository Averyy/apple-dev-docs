# fieldName()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the internal field name associated with the widget annotation.

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

The internal field name associated with the widget annotation.

#### Discussion

If the widget annotation is backed by PDF form data, it can associate an optional field name with a value or other data.

## See Also

### Managing the Associated Field Name
- [func setFieldName(String!)](./setfieldname%28_%29.md)
  Sets the internal field name associated with the widget annotation’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/fieldname())*