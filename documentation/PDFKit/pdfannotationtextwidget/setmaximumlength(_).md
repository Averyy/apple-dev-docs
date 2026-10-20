# setMaximumLength(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the maximum number of characters allowed in the annotation string.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setMaximumLength(_ maxLen: Int)
```

```objc
- (void) setMaximumLength:(NSUInteger) maxLen;
```

## Parameters

- `maxLen`: The maximum number of characters allowed in the annotation string. Pass `0` to indicate that there is no specified maximum.

## See Also

### Related Documentation
- [class PDFAnnotationTextWidget](../pdfannotationtextwidget.md)
  A `PDFAnnotationTextWidget` object allows you to manage the appearance and content of text fields.
### Working with Annotation Strings
- [func stringValue() -> String!](./stringvalue%28%29.md)
  Returns the string assigned to the annotation.
- [func setStringValue(String!)](./setstringvalue%28_%29.md)
  Sets the string for the annotation.
- [func maximumLength() -> Int](./maximumlength%28%29.md)
  Returns the maximum number of characters allowed in the annotation string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationtextwidget/setmaximumlength(_:))*