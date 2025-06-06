# NSTabViewController

**Framework**: AppKit  
**Kind**: class

A container view controller that manages a tab view interface, which organizes multiple pages of content but displays only one page at a time.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSTabViewController
```

#### Overview

Each page of content is managed by a separate child view controller. Navigation between child view controllers is accomplished with the help of an [`NSTabView`](nstabview.md) object, which the tab view controller manages. When the user selects a new tab, the tab view controller displays the content associated with the associated child view controller, replacing the previous content.

Each tab is represented by an [`NSTabViewItem`](nstabviewitem.md) object, which contains the name of the tab and stores a pointer to the child view controller that manages the tab’s content. Normally, you configure the tab view items at design time using Interface Builder, but you can also add them programmatically using the methods of this class. Always assign a child view controller to new tab view items before adding those items to the tab view interface.

Another way to add tabs programmatically is to add child view controllers directly to the tab view controller. When you call the [`addChild(_:)`](nsviewcontroller/addchild(_:).md) or [`insertChild(_:at:)`](nsviewcontroller/insertchild(_:at:).md) method of this class, the tab view controller automatically creates a default [`NSTabViewItem`](nstabviewitem.md) object for the specified view controller. You can fetch the newly created item using the [`tabViewItem(for:)`](nstabviewcontroller/tabviewitem(for:).md) method and configure it. Removing a child view controller with the [`removeChild(at:)`](nsviewcontroller/removechild(at:).md) method similarly removes the corresponding tab view item.

The tab view controller lazily loads the views associated with each child view controller, creating them only after the corresponding tab is selected. When the tab view controller’s view is first displayed, only the view for the initially selected tab is loaded.

The [`tabStyle`](nstabviewcontroller/tabstyle-swift.property.md) property determines the appearance of the tab controls. A tab view controller can display a segmented control or display tabs in the window’s toolbar. You can also provide your own control for displaying tabs. The tab view controller automatically coordinates interactions between designated control and the corresponding [`tabView`](nstabviewcontroller/tabview.md) object.

## Topics

### Configuring the Tab View
- [var tabStyle: NSTabViewController.TabStyle](nstabviewcontroller/tabstyle-swift.property.md)
  The style used to display the tabs.
- [var tabView: NSTabView](nstabviewcontroller/tabview.md)
  The tab view that manages the views of the interface.
- [var transitionOptions: NSViewController.TransitionOptions](nstabviewcontroller/transitionoptions.md)
  The animation options to use when switching between tabs.
- [var canPropagateSelectedChildViewControllerTitle: Bool](nstabviewcontroller/canpropagateselectedchildviewcontrollertitle.md)
  A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.
### Managing Tab View Items
- [var tabViewItems: [NSTabViewItem]](nstabviewcontroller/tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](nstabviewcontroller/tabviewitem(for:).md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](nstabviewcontroller/addtabviewitem(_:).md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabviewcontroller/inserttabviewitem(_:at:).md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](nstabviewcontroller/removetabviewitem(_:).md)
  Removes the specified tab view item from the tab view controller.
- [var selectedTabViewItemIndex: Int](nstabviewcontroller/selectedtabviewitemindex.md)
  The index of the selected tab.
### Responding to Tab View Events
- [func viewDidLoad()](nstabviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewcontroller/tabview(_:shouldselect:).md)
  Asks the tab view controller if the specified tab should be selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](nstabviewcontroller/tabview(_:willselect:).md)
  Informs the tab view controller that the specified tab is about to be selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](nstabviewcontroller/tabview(_:didselect:).md)
  Informs the tab view controller that the specified tab was selected.
### Responding to Toolbar Events
- [func toolbar(NSToolbar, itemForItemIdentifier: NSToolbarItem.Identifier, willBeInsertedIntoToolbar: Bool) -> NSToolbarItem?](nstabviewcontroller/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md)
  Returns the toolbar item for the specified identifier.
- [func toolbarAllowedItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbaralloweditemidentifiers(_:).md)
  Returns the array of identifier strings for the allowed toolbar items.
- [func toolbarDefaultItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbardefaultitemidentifiers(_:).md)
  Returns the array of identifier strings for the default toolbar items.
- [func toolbarSelectableItemIdentifiers(NSToolbar) -> [NSToolbarItem.Identifier]](nstabviewcontroller/toolbarselectableitemidentifiers(_:).md)
  Returns the array of identifier strings for the selectable toolbar items
### Constants
- [NSTabViewController.TabStyle](nstabviewcontroller/tabstyle-swift.enum.md)
  Tab control style options for a tab view controller.

## Relationships

### Inherits From
- [NSViewController](nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](nssegueperforming.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTabViewDelegate](nstabviewdelegate.md)
- [NSToolbarDelegate](nstoolbardelegate.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSTabView](nstabview.md)
  A multipage interface that displays one page at a time.
- [class NSTabViewItem](nstabviewitem.md)
  An item in a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller)*