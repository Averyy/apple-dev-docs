# setStringValue(_:)

**Framework**: PDFKit  
**Kind**: method

Sets the selection in the widget annotation.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setStringValue(_ value: String!)
```

#### Discussion

If the widget annotation object is backed by PDF form data, this method updates the value associated with the appropriate field in the form object.

## Parameters

- `value`: The string that represents the selection in the widget annotation.

## See Also

- [func stringValue() -> String!](pdfannotationchoicewidget/stringvalue.md)
  Returns the selection in the widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/setstringvalue(_:))*