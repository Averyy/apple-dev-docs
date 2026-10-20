# UIContextualAction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An action to display when the user swipes a table row.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIContextualAction
```

```objc
@interface UIContextualAction : NSObject
```

#### Overview

Create [`UIContextualAction`](./uicontextualaction.md) objects to define the types of actions that can be performed when the user swipes left or right on a table row. Use your actions to initialize a [`UISwipeActionsConfiguration`](./uiswipeactionsconfiguration.md) object in your table view delegate object.

## Topics

### Creating the contextual action
- [convenience init(style: UIContextualAction.Style, title: String?, handler: UIContextualAction.Handler)](./uicontextualaction/init%28style,title,handler%29.md)
  Creates a new contextual action with the specified title and handler.
### Configuring the appearance
- [var title: String?](./uicontextualaction/title.md)
  The title displayed on the action button.
- [var backgroundColor: UIColor!](./uicontextualaction/backgroundcolor.md)
  The background color of the action button.
- [var image: UIImage?](./uicontextualaction/image.md)
  The image to display in the action button.
### Getting the configuration details
- [var handler: UIContextualAction.Handler](./uicontextualaction/handler-swift.property.md)
  The handler block to execute when the user selects the action.
- [UIContextualAction.Handler](./uicontextualaction/handler-swift.typealias.md)
  The handler block to call in response to the selection of an action.
- [var style: UIContextualAction.Style](./uicontextualaction/style-swift.property.md)
  The style that applies to the action button.
- [UIContextualAction.Style](./uicontextualaction/style-swift.enum.md)
  Constants indicating the style information that applies to the action button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Row actions
- [class UISwipeActionsConfiguration](./uiswipeactionsconfiguration.md)
  The set of actions to perform when swiping on rows of a table.
- [class UITableViewRowAction](./uitableviewrowaction.md)
  A single action to present when the user swipes horizontally in a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction)*