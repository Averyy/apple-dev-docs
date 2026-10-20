# UIDocumentMenuOrder

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The insertion point for custom menu items.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
enum UIDocumentMenuOrder
```

```c
enum UIDocumentMenuOrder : NSUInteger;
```

## Topics

### Constants
- [UIDocumentMenuOrder.first](./uidocumentmenuorder/first.md)
  The top item in the document menu.
- [UIDocumentMenuOrder.last](./uidocumentmenuorder/last.md)
  The bottom item in the document menu.
### Initializers
- [init?(rawValue: UInt)](./uidocumentmenuorder/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a document menu
- [func addOption(withTitle: String, image: UIImage?, order: UIDocumentMenuOrder, handler: () -> Void)](./uidocumentmenuviewcontroller/addoption%28withtitle,image,order,handler%29.md)
  Adds a custom menu item to the list of document pickers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuorder)*