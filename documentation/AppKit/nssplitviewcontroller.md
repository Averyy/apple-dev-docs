# NSSplitViewController

**Framework**: AppKit  
**Kind**: class

An object that manages an array of adjacent child views, and has a split view object for managing dividers between those views.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NSSplitViewController
```

#### Overview

A split view controller manages a set of child views that it displays next to each other in a side-by-side or top-to-bottom arrangement.

A split view controller owns an array of split view items ([`NSSplitViewItem`](nssplitviewitem.md)), each of which has a view controller ([`NSViewController`](nsviewcontroller.md)) and corresponding view. The split view controller’s [`splitView`](nssplitviewcontroller/splitview.md) object manages those child views and the dividers between them.

By default, a split view arranges its child views vertically from top to bottom. To specify a horizontal (side-by-side) arrangement, implement the [`isVertical`](nssplitview/isvertical.md) property of the [`splitView`](nssplitviewcontroller/splitview.md) object to return [`true`](https://developer.apple.com/documentation/swift/true).

The split view controller serves as the delegate of its [`splitView`](nssplitviewcontroller/splitview.md) object. If you override a split view delegate method, your override must call `super`.

To use a split view controller, you must use Auto Layout for the child views and to support animations that collapse and reveal child views. For example, if you design a layout that contains two views, a content area and an optional sidebar, you employ Auto Layout constraints to specify whether the content area shrinks or remains the same size when the sidebar becomes visible.

A split view controller employs lazy loading of its views. For example, adding a collapsed split view item as a new child doesn’t load the associated view until it shows.

For more information about using [`NSSplitViewController`](nssplitviewcontroller.md) in your app, see [`Navigating Hierarchical Data Using Outline and Split Views`](navigating-hierarchical-data-using-outline-and-split-views.md).

## Topics

### Configuring and Managing a Split View Controller
- [var splitView: NSSplitView](nssplitviewcontroller/splitview.md)
  The split view that the split view controller manages.
- [func splitViewItem(for: NSViewController) -> NSSplitViewItem?](nssplitviewcontroller/splitviewitem(for:).md)
  Returns the corresponding split view item for the specified child view controller of the split view controller.
- [var splitViewItems: [NSSplitViewItem]](nssplitviewcontroller/splitviewitems.md)
  The array of split view items that correspond to the split view controller’s child view controllers.
- [class NSSplitViewItem](nssplitviewitem.md)
  An item in a split view controller.
### Modifying a Split View Controller
- [func addSplitViewItem(NSSplitViewItem)](nssplitviewcontroller/addsplitviewitem(_:).md)
  Adds a split view item to the end of the array of split view items.
- [func insertSplitViewItem(NSSplitViewItem, at: Int)](nssplitviewcontroller/insertsplitviewitem(_:at:).md)
  Adds a split view item to the array of split view items at the specified index position.
- [func removeSplitViewItem(NSSplitViewItem)](nssplitviewcontroller/removesplitviewitem(_:).md)
  Removes a specified split view item from the split view controller.
### Managing Sidebars
- [func toggleSidebar(Any?)](nssplitviewcontroller/togglesidebar(_:).md)
  Collapses or expands the first sidebar in the split view controller using an animation.
- [var minimumThicknessForInlineSidebars: CGFloat](nssplitviewcontroller/minimumthicknessforinlinesidebars.md)
  The minimum thickness for a sidebar before it automatically collapses.
- [class let automaticDimension: CGFloat](nssplitviewcontroller/automaticdimension.md)
  The default value to apply to a dimension.
### Managing Inspectors
- [func toggleInspector(Any?)](nssplitviewcontroller/toggleinspector(_:).md)
### Responding to View Events
- [func viewDidLoad()](nssplitviewcontroller/viewdidload.md)
  Configures the split view controller after its view loads into memory.
### Supporting Protocol Requirements
- [Protocol Implementations](nssplitviewcontroller-protocol-implementations.md)
  Access the split view controller’s implementations of protocol methods.

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
- [NSSplitViewDelegate](nssplitviewdelegate.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSSplitView](nssplitview.md)
  A view that arranges two or more views in a linear stack running horizontally or vertically.
- [class NSSplitViewItem](nssplitviewitem.md)
  An item in a split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller)*