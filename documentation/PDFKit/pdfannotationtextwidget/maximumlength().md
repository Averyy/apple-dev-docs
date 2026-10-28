# maximumLength()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the maximum number of characters allowed in the annotation string.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func maximumLength() -> Int
```

```objc
- (NSUInteger) maximumLength;
```

## Return Value

The maximum number of characters allowed in the annotations string. A return value of `0` means that there is no specified maximum.

## See Also

### Related Documentation
- [class PDFAnnotationTextWidget](../pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
### Working with Annotation Strings
- [func stringValue() -> String!](./stringvalue%28%29.md)
  Returns the string assigned to the annotation.
- [func setStringValue(String!)](./setstringvalue%28_%29.md)
  Sets the string for the annotation.
- [func setMaximumLength(Int)](./setmaximumlength%28_%29.md)
  Sets the maximum number of characters allowed in the annotation string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/maximumlength())*