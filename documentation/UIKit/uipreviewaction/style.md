# UIPreviewAction.Style

**Framework**: UIKit  
**Kind**: enum

The style for a peek quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
enum Style
```

#### Overview

Use these styles with instances of the [`UIPreviewAction`](uipreviewaction.md) and [`UIPreviewActionGroup`](uipreviewactiongroup.md) classes.

## Topics

### Constants
- [UIPreviewAction.Style.default](uipreviewaction/style/default.md)
  The default style.
- [UIPreviewAction.Style.selected](uipreviewaction/style/selected.md)
  The style for a selected peek quick action.
- [UIPreviewAction.Style.destructive](uipreviewaction/style/destructive.md)
  The style for a peek quick action that changes or deletes data.
### Initializers
- [init?(rawValue: Int)](uipreviewaction/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(title: String, style: UIPreviewAction.Style, handler: (UIPreviewAction, UIViewController) -> Void)](uipreviewaction/init(title:style:handler:).md)
  Creates a peek quick action using a specified title, style, and handler.
- [var handler: (any UIPreviewActionItem, UIViewController) -> Void](uipreviewaction/handler.md)
  The block called when the peek quick action is selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewaction/style)*