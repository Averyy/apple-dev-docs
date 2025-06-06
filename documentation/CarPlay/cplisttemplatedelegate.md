# CPListTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol

The interface an object implements to serve as the delegate for a list template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol CPListTemplateDelegate : NSObjectProtocol
```

## Topics

### Getting the Selected Item
- [func listTemplate(CPListTemplate, didSelect: CPListItem, completionHandler: () -> Void)](cplisttemplatedelegate/listtemplate(_:didselect:completionhandler:).md)
  Tells the delegate when the user selects a list item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CPListTemplateDelegate)?](cplisttemplate/delegate.md)
  The object that serves as the delegate to the list template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedelegate)*