# NSTabViewItem

**Framework**: AppKit  
**Kind**: class

An item in a tab view.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSTabViewItem
```

#### Overview

An [`NSTabViewItem`](nstabviewitem.md) is a convenient way for presenting information in multiple pages. A tab view is usually distinguished by a row of tabs that give the visual appearance of folder tabs. When the user clicks a tab, the tab view displays a view page provided by your application. A tab view keeps a zero-based array of tab view items, one for each tab in the view.

## Topics

### Creating a Tab View Item
- [init(identifier: Any?)](nstabviewitem/init(identifier:).md)
  Performs default initialization for the receiver.
### Working with Labels
- [func drawLabel(Bool, in: NSRect)](nstabviewitem/drawlabel(_:in:).md)
  Draws the receiver’s label in `tabRect`, which is the area between the curved end caps.
- [var label: String](nstabviewitem/label.md)
  Sets the label text for the receiver to `label`.
- [func sizeOfLabel(Bool) -> NSSize](nstabviewitem/sizeoflabel(_:).md)
  Calculates the size of the receiver’s label.
### Checking the Tab Display State
- [var tabState: NSTabViewItem.State](nstabviewitem/tabstate.md)
  Returns the current display state of the tab associated with the receiver.
### Assigning an Identifier Object
- [var identifier: Any?](nstabviewitem/identifier.md)
  Sets the receiver’s optional identifier object to `identifier`.
### Setting the Color
- [var color: NSColor](nstabviewitem/color.md)
  Sets the background color for content in the view.
### Assigning a View
- [var view: NSView?](nstabviewitem/view.md)
  Sets the view associated with the receiver to `view`.
### Setting the Initial First Responder
- [var initialFirstResponder: NSView?](nstabviewitem/initialfirstresponder.md)
  Sets the initial first responder for the view associated with the receiver (the view that is displayed when a user clicks on the tab) to `view`.
### Accessing the Parent Tab View
- [var tabView: NSTabView?](nstabviewitem/tabview.md)
  Returns the parent tab view for the receiver.
### Getting and Setting Tooltips
- [var toolTip: String?](nstabviewitem/tooltip.md)
  Sets the tooltip displayed for the tab view item.
### Constants
- [NSTabViewItem.State](nstabviewitem/state.md)
  These constants describe the current display state of a tab:
### Initializers
- [convenience init(viewController: NSViewController)](nstabviewitem/init(viewcontroller:).md)
### Instance Properties
- [var image: NSImage?](nstabviewitem/image.md)
- [var viewController: NSViewController?](nstabviewitem/viewcontroller.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTabViewController](nstabviewcontroller.md)
  A container view controller that manages a tab view interface, which organizes multiple pages of content but displays only one page at a time.
- [class NSTabView](nstabview.md)
  A multipage interface that displays one page at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem)*