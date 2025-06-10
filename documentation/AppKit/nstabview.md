# NSTabView

**Framework**: AppKit  
**Kind**: class

A multipage interface that displays one page at a time.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTabView
```

#### Overview

A tab view contains a row of tabs that give the appearance of folder tabs, as shown in the [`Figure 1`](nstabview#2555818.md). The user selects the desired page by clicking the appropriate tab or using the arrow keys to move between pages. Each page displays a view hierarchy provided by your app.

![None](https://docs-assets.developer.apple.com/published/32a0de8ad83145bde674bf96a45ecdb7/media-2555818%402x.png)

## Topics

### Handling the Selection of Tabs
- [var delegate: (any NSTabViewDelegate)?](nstabview/delegate.md)
  The tab view’s delegate.
- [protocol NSTabViewDelegate](nstabviewdelegate.md)
  The `NSTabViewDelegate` protocol defines the optional methods implemented by delegates of `NSTabView` objects.
### Adding and Removing Tabs
- [func addTabViewItem(NSTabViewItem)](nstabview/addtabviewitem(_:).md)
  Adds the specified tab item.
- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func removeTabViewItem(NSTabViewItem)](nstabview/removetabviewitem(_:).md)
  Removes the specified item from the tab view’s array of tab view items.
### Accessing Tabs
- [func indexOfTabViewItem(NSTabViewItem) -> Int](nstabview/indexoftabviewitem(_:).md)
  Returns the index of the specified item in the tab view.
- [func indexOfTabViewItem(withIdentifier: Any) -> Int](nstabview/indexoftabviewitem(withidentifier:).md)
  Returns the index of the item that matches the specified identifier or `NSNotFound` if the item is not found.
- [var numberOfTabViewItems: Int](nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.
- [func tabViewItem(at: Int) -> NSTabViewItem](nstabview/tabviewitem(at:)-7r3at.md)
  Returns the tab view item at `index` in the tab view’s array of items.
- [var tabViewItems: [NSTabViewItem]](nstabview/tabviewitems.md)
  The tab view’s array of tab view items.
### Configuring the Tab Attributes
- [var tabViewType: NSTabView.TabType](nstabview/tabviewtype.md)
  The tab type to display the tabs.
- [NSTabView.TabType](nstabview/tabtype.md)
  These constants specify the tab view’s type as used by the [`tabViewType`](nstabview/tabviewtype.md) property.
- [var tabPosition: NSTabView.TabPosition](nstabview/tabposition-swift.property.md)
- [NSTabView.TabPosition](nstabview/tabposition-swift.enum.md)
- [var tabViewBorderType: NSTabView.TabViewBorderType](nstabview/tabviewbordertype-swift.property.md)
- [NSTabView.TabViewBorderType](nstabview/tabviewbordertype-swift.enum.md)
### Selecting a Tab
- [func selectFirstTabViewItem(Any?)](nstabview/selectfirsttabviewitem(_:).md)
  This action method selects the first tab view item.
- [func selectLastTabViewItem(Any?)](nstabview/selectlasttabviewitem(_:).md)
  This action method selects the last tab view item.
- [func selectNextTabViewItem(Any?)](nstabview/selectnexttabviewitem(_:).md)
  This action method selects the next tab view item in the sequence.
- [func selectPreviousTabViewItem(Any?)](nstabview/selectprevioustabviewitem(_:).md)
  This action method selects the previous tab view item in the sequence.
- [func selectTabViewItem(NSTabViewItem?)](nstabview/selecttabviewitem(_:).md)
  Selects the specified tab view item.
- [func selectTabViewItem(at: Int)](nstabview/selecttabviewitem(at:).md)
  Selects the tab view item specified by `index`.
- [func selectTabViewItem(withIdentifier: Any)](nstabview/selecttabviewitem(withidentifier:).md)
  Selects the tab view item specified by `identifier`.
- [var selectedTabViewItem: NSTabViewItem?](nstabview/selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](nstabview/takeselectedtabviewitemfromsender(_:).md)
  Sets the selected tab view item to the selected item obtained from the sender.
### Modifying the Font
- [var font: NSFont](nstabview/font.md)
  The font used for the tab view’s label text.
### Modifying Controls Tint
- [var controlTint: NSControlTint](nstabview/controltint.md)
  The tab view’s control tint.
### Manipulating the Background
- [var drawsBackground: Bool](nstabview/drawsbackground.md)
  A Boolean value that indicates if the tab view draws a background color when its type is `NSNoTabsNoBorder`.
### Determining the Size
- [var minimumSize: NSSize](nstabview/minimumsize.md)
  The minimum size necessary for the tab view to display tabs in a useful way.
- [var contentRect: NSRect](nstabview/contentrect.md)
  The rectangle describing the content area of the tab view.
- [var controlSize: NSControl.ControlSize](nstabview/controlsize.md)
  The size of the tab view.
### Truncating Tab Labels
- [var allowsTruncatedLabels: Bool](nstabview/allowstruncatedlabels.md)
  A Boolean value that indicates if the tab view allows truncating for labels that don’t fit on a tab.
### Event Handling
- [func tabViewItem(at: NSPoint) -> NSTabViewItem?](nstabview/tabviewitem(at:)-8gnqw.md)
  Returns the tab view item at the specified point.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTabViewController](nstabviewcontroller.md)
  A container view controller that manages a tab view interface, which organizes multiple pages of content but displays only one page at a time.
- [class NSTabViewItem](nstabviewitem.md)
  An item in a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview)*