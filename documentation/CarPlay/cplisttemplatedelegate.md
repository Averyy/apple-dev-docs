# CPListTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

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

### Getting the selected item
- [func listTemplate(CPListTemplate, didSelect: CPListItem, completionHandler: () -> Void)](./cplisttemplatedelegate/listtemplate%28_,didselect,completionhandler%29.md)
  The user has selected an item in the list template.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated
- [var delegate: (any CPListTemplateDelegate)?](./cplisttemplate/delegate.md)
  The list template’s delegate is informed of list selection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedelegate)*