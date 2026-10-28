# caption()

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the text of the label on a push button control.

**Availability**:
- macOS 10.4+ - Deprecated in 10.12

## Declaration

```swift
func caption() -> String!
```

```objc
- (NSString *) caption;
```

## Return Value

The label drawn on a push button control.

## Discussion

This method applies only to the label drawn on a control of type [`PDFAnnotationButtonWidget`](../pdfannotationbuttonwidget.md).

## See Also

### Related Documentation
- [class PDFAnnotationButtonWidget](../pdfannotationbuttonwidget.md)
  A `PDFAnnotationButtonWidget` object provides user interactivity on a page of a PDF document. There are three types of buttons available: push button, radio button, and checkbox.
### Getting and Setting the Control Label Text
- [func setCaption(String!)](./setcaption%28_%29.md)
  Sets the text of the label on a push button control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationbuttonwidget/caption())*