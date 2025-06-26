# UIDocumentBrowserAction

**Framework**: UIKit  
**Kind**: class

A custom action that you can create and add to a document browser’s Edit menu or navigation bar.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class UIDocumentBrowserAction
```

## Mentions

- [Adding custom actions and activities](adding-custom-actions-and-activities.md)

#### Overview

By default, the system provides a number of standard actions (copy, move, rename, delete, and share). To add custom actions, assign an array of [`UIDocumentBrowserAction`](uidocumentbrowseraction.md) objects to the browser’s [`customActions`](uidocumentbrowserviewcontroller/customactions.md) property.

Document browser actions can appear in either the navigation bar or the Edit menu.

-  actions appear in the navigation bar when the user places the browser into the Select mode.
-  actions appear in the Edit Menu when the user long presses on a document or folder.

When triggered, these actions are passed the URLs of the currently selected items.

## Topics

### Creating and configuring actions
- [init(identifier: String, localizedTitle: String, availability: UIDocumentBrowserAction.Availability, handler: ([URL]) -> Void)](uidocumentbrowseraction/init(identifier:localizedtitle:availability:handler:).md)
  Instantiates and returns a new browser action item.
- [var image: UIImage?](uidocumentbrowseraction/image.md)
  The action’s image displayed in the navigation bar.
- [var supportedContentTypes: [String]](uidocumentbrowseraction/supportedcontenttypes.md)
  An array of uniform type identifiers that define the types of documents that the action supports.
- [var supportsMultipleItems: Bool](uidocumentbrowseraction/supportsmultipleitems.md)
  A Boolean value that determines whether the action can be triggered on more than one document at a time.
### Accessing activity data
- [var identifier: String](uidocumentbrowseraction/identifier.md)
  The action’s unique identifier.
- [var localizedTitle: String](uidocumentbrowseraction/localizedtitle.md)
  The title that appears in the menu or navigation bar.
- [var availability: UIDocumentBrowserAction.Availability](uidocumentbrowseraction/availability-swift.property.md)
  A value that defines where the action can appear (in the Edit Menu, the navigation bar, or both).
- [UIDocumentBrowserAction.Availability](uidocumentbrowseraction/availability-swift.struct.md)
  Values that determine where the action can appear in the document browser.
### Instance Properties
- [var imageOnlyForContextMenu: UIImage?](uidocumentbrowseraction/imageonlyforcontextmenu.md)

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

## See Also

- [class UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [var customActions: [UIDocumentBrowserAction]](uidocumentbrowserviewcontroller/customactions.md)
  Custom document browser actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction)*