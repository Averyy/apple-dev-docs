# UIPreviewParameters

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Additional parameters to use when animating a preview interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPreviewParameters
```

```objc
@interface UIPreviewParameters : NSObject
```

## Topics

### Creating preview parameters
- [init()](./uipreviewparameters/init%28%29.md)
  Creates a default set of preview parameters.
- [convenience init(textLineRects: [NSValue])](./uipreviewparameters/init%28textlinerects%29.md)
  Creates a preview parameters object with information about the text you want to preview.
### Configuring the preview attributes
- [var backgroundColor: UIColor!](./uipreviewparameters/backgroundcolor.md)
  The background color to display behind the preview.
- [var visiblePath: UIBezierPath?](./uipreviewparameters/visiblepath.md)
  The portion of the view to show in the preview.
- [var shadowPath: UIBezierPath?](./uipreviewparameters/shadowpath.md)
  The path to use for drawing the preview’s shadow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIDragPreviewParameters](./uidragpreviewparameters.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Contextual menus
- [class UIContextMenuSystem](./uicontextmenusystem.md)
  The context menu system.
- [class UIContextMenuInteraction](./uicontextmenuinteraction.md)
  An interaction object that you use to display relevant actions for your content.
- [protocol UIContextMenuInteractionDelegate](./uicontextmenuinteractiondelegate.md)
  The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [class UITargetedPreview](./uitargetedpreview.md)
  An object describing the view to use during preview-related animations.
- [class UIPreviewTarget](./uipreviewtarget.md)
  An object that specifies the container view to use for animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters)*