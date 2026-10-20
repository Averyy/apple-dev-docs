# setStringValue(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the selection in the widget annotation.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setStringValue(_ value: String!)
```

```objc
- (void) setStringValue:(NSString *) value;
```

#### Discussion

If the widget annotation object is backed by PDF form data, this method updates the value associated with the appropriate field in the form object.

## Parameters

- `value`: The string that represents the selection in the widget annotation.

## See Also

### Getting and Setting the String Value
- [func stringValue() -> String!](./stringvalue%28%29.md)
  Returns the selection in the widget annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationchoicewidget/setstringvalue(_:))*