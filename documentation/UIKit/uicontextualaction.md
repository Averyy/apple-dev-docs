# UIContextualAction

**Framework**: UIKit  
**Kind**: class

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

#### Overview

Create [`UIContextualAction`](uicontextualaction.md) objects to define the types of actions that can be performed when the user swipes left or right on a table row. Use your actions to initialize a [`UISwipeActionsConfiguration`](uiswipeactionsconfiguration.md) object in your table view delegate object.

## Topics

### Creating the contextual action
- [convenience init(style: UIContextualAction.Style, title: String?, handler: UIContextualAction.Handler)](uicontextualaction/init(style:title:handler:).md)
  Creates a new contextual action with the specified title and handler.
### Configuring the appearance
- [var title: String?](uicontextualaction/title.md)
  The title displayed on the action button.
- [var backgroundColor: UIColor!](uicontextualaction/backgroundcolor.md)
  The background color of the action button.
- [var image: UIImage?](uicontextualaction/image.md)
  The image to display in the action button.
### Getting the configuration details
- [var handler: UIContextualAction.Handler](uicontextualaction/handler-swift.property.md)
  The handler block to execute when the user selects the action.
- [UIContextualAction.Handler](uicontextualaction/handler-swift.typealias.md)
  The handler block to call in response to the selection of an action.
- [var style: UIContextualAction.Style](uicontextualaction/style-swift.property.md)
  The style that applies to the action button.
- [UIContextualAction.Style](uicontextualaction/style-swift.enum.md)
  Constants indicating the style information that applies to the action button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UISwipeActionsConfiguration](uiswipeactionsconfiguration.md)
  The set of actions to perform when swiping on rows of a table.
- [class UITableViewRowAction](uitableviewrowaction.md)
  A single action to present when the user swipes horizontally in a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction)*