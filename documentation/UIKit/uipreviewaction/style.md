# UIPreviewAction.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The style for a peek quick action.

**Availability**:
- iOS 9.0+ - Deprecated in 17.1
- iPadOS 9.0+ - Deprecated in 17.1
- Mac Catalyst 13.1+ - Deprecated in 17.1
- tvOS 9.0+ - Deprecated in 17.1

> **Deprecated**: For more information, see [`UIPreviewAction`](../uipreviewaction.md).

## Declaration

```swift
enum Style
```

```c
enum UIPreviewActionStyle : NSInteger;
```

#### Overview

Use these styles with instances of the [`UIPreviewAction`](../uipreviewaction.md) and [`UIPreviewActionGroup`](../uipreviewactiongroup.md) classes.

## Topics

### Constants
- [UIPreviewAction.Style.default](./style/default.md)
  The default style.
- [UIPreviewAction.Style.selected](./style/selected.md)
  The style for a selected peek quick action.
- [UIPreviewAction.Style.destructive](./style/destructive.md)
  The style for a peek quick action that changes or deletes data.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a peek quick action
- [convenience init(title: String, style: UIPreviewAction.Style, handler: (UIPreviewAction, UIViewController) -> Void)](./init%28title,style,handler%29.md)
  Creates a peek quick action using a specified title, style, and handler.
- [var handler: (any UIPreviewActionItem, UIViewController) -> Void](./handler.md)
  The block called when the peek quick action is selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewaction/style)*