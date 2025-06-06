# UIPreviewActionItem

**Framework**: UIKit  
**Kind**: protocol

A set of methods that defines the styles you can apply to peek quick actions and peek quick action groups, and defines a read-only accessor for the user-visible title of a peek quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIPreviewActionItem : NSObjectProtocol
```

#### Overview

> ❗ **Important**:  Don’t adopt this protocol in custom classes.

 Don’t adopt this protocol in custom classes.

The [`UIPreviewActionItem`](uipreviewactionitem.md) protocol is adopted by the [`UIPreviewAction`](uipreviewaction.md) and [`UIPreviewActionGroup`](uipreviewactiongroup.md) classes.

## Topics

### Accessing peek quick action properties
- [var title: String](uipreviewactionitem/title.md)
  The peek quick action item’s title.
### Constants
- [UIPreviewAction.Style](uipreviewaction/style.md)
  The style for a peek quick action.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIPreviewAction](uipreviewaction.md)
- [UIPreviewActionGroup](uipreviewactiongroup.md)

## See Also

- [class UIPreviewInteraction](uipreviewinteraction.md)
  A class that registers a view to provide a custom user experience in response to 3D Touch interactions.
- [protocol UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md)
  A set of methods for communicating the progress of a preview interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewactionitem)*