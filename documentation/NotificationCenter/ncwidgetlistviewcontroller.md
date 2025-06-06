# NCWidgetListViewController

**Framework**: Notification Center  
**Kind**: class

An object that provides a list view for displaying content in a macOS Today widget.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NCWidgetListViewController
```

#### Overview

The `NCWidgetListViewController` class provides a list view for displaying content in a Today widget. A list view controller works together with its delegate to display content and support user interaction with the list. To learn about the list view controller delegate methods, see [`NCWidgetListViewDelegate`](ncwidgetlistviewdelegate.md).

You store the contents of a widget as an array of objects in the list view controller’s [`contents`](ncwidgetlistviewcontroller/contents.md) property. To display the objects, you use a [`delegate`](ncwidgetlistviewcontroller/delegate.md) object, which provides a custom view controller for each object in `contents`. A list view controller also provides properties that make it easy to specify aspects of the list’s appearance and behavior, such as the number of rows to display, the presence of divider lines, and the ability to edit the list.

## Topics

### Displaying and Editing List Content
- [var delegate: (any NCWidgetListViewDelegate)?](ncwidgetlistviewcontroller/delegate.md)
  The list view controller’s delegate or `nil` if the receiver doesn’t have a delegate.
- [protocol NCWidgetListViewDelegate](ncwidgetlistviewdelegate.md)
  The interface for handling content display and editing in the list view of a macOS Today widget.
### Accessing Content
- [var contents: [Any]](ncwidgetlistviewcontroller/contents.md)
  An array of objects to display in the list view.
- [func row(for: NSViewController) -> Int](ncwidgetlistviewcontroller/row(for:).md)
  Returns the row represented by the specified content view controller.
- [func viewController(atRow: Int, makeIfNecessary: Bool) -> NSViewController](ncwidgetlistviewcontroller/viewcontroller(atrow:makeifnecessary:).md)
  Returns the content view controller associated with the specified row, or a new content view controller if desired.
### Customizing the List Appearance
- [var minimumVisibleRowCount: Int](ncwidgetlistviewcontroller/minimumvisiblerowcount.md)
  The minimum number of visible rows to display.
- [var hasDividerLines: Bool](ncwidgetlistviewcontroller/hasdividerlines.md)
  A Boolean value that indicates whether list displays divider lines between rows.
### Supporting Editing
- [var editing: Bool](ncwidgetlistviewcontroller/editing.md)
  A Boolean value that indicates whether the list is in editing mode.
- [var showsAddButtonWhenEditing: Bool](ncwidgetlistviewcontroller/showsaddbuttonwhenediting.md)
  A Boolean value that indicates whether an Add (+) button is displayed while the list is in editing mode.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller)*