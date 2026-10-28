# setState(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the state of the control.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func setState(_ value: Int)
```

```objc
- (void) setState:(NSInteger) value;
```

## Discussion

A control’s state (for example, checked or unchecked) affects how it is drawn. Note that push buttons are always in the on state.

## Parameters

- `value`: The state the control should be in.

## See Also

### Getting and Setting the Control’s State
- [func state() -> Int](./state%28%29.md)
  Returns the state of the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget/setstate(_:))*