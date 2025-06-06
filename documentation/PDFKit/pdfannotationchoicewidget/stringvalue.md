# stringValue()

**Framework**: PDFKit  
**Kind**: method

Returns the selection in the widget annotation.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func stringValue() -> String!
```

#### Return Value

The string that represents the selection in the widget annotation.

#### Discussion

If the widget annotation object is backed by PDF form data, this method returns the value associated with the appropriate field in the form object, if possible.

## See Also

- [func setStringValue(String!)](pdfannotationchoicewidget/setstringvalue(_:).md)
  Sets the selection in the widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/stringvalue())*