# CPListTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The interface an object implements to serve as the delegate for a list template.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
protocol CPListTemplateDelegate : NSObjectProtocol
```

```objc
@protocol CPListTemplateDelegate <NSObject>
```

## Topics

### Getting the Selected Item
- [func listTemplate(CPListTemplate, didSelect: CPListItem, completionHandler: () -> Void)](./cplisttemplatedelegate/listtemplate%28_,didselect,completionhandler%29.md)
  Tells the delegate when the user selects a list item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to List Events
- [var delegate: (any CPListTemplateDelegate)?](./cplisttemplate/delegate.md)
  The object that serves as the delegate to the list template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedelegate)*