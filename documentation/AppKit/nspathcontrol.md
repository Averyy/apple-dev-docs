# NSPathControl

**Framework**: AppKit  
**Kind**: class

A display of a file system path or virtual path information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class NSPathControl
```

#### Overview

The [`NSPathControl`](nspathcontrol.md) class uses [`NSPathCell`](nspathcell.md) to implement its user interface. [`NSPathControl`](nspathcontrol.md) provides cover methods for most [`NSPathCell`](nspathcell.md) methods—the cover method simply invokes the corresponding cell method. See also [`NSPathComponentCell`](nspathcomponentcell.md), which represents individual components of the path, and two associated protocols: [`NSPathCellDelegate`](nspathcelldelegate.md) and [`NSPathControlDelegate`](nspathcontroldelegate.md).

[`NSPathControl`](nspathcontrol.md) has three styles represented by the [`NSPathControl.Style`](nspathcontrol/style.md) enumeration constants [`NSPathControl.Style.standard`](nspathcontrol/style/standard.md), [`NSPathStyleNavigationBar`](nspathstyle/nspathstylenavigationbar.md), and [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md). The represented path can be a file system path or any other type of path leading through a sequence of nodes or components, as defined by the programmer.

[`NSPathControl`](nspathcontrol.md) automatically supports drag and drop, which can be further customized via delegate methods. To accept drag and drop, [`NSPathControl`](nspathcontrol.md) calls [`registerForDraggedTypes(_:)`](nsview/registerfordraggedtypes(_:).md) with [`NSFilenamesPboardType`](nsfilenamespboardtype.md) and [`NSURLPboardType`](nsurlpboardtype.md). When the URL value in the [`NSPathControl`](nspathcontrol.md) object changes because of an automatic drag and drop operation or the user selecting a new path via the open panel, the action is sent. In OS X v10.5 the value returned by [`clickedPathComponentCell()`](nspathcontrol/clickedpathcomponentcell().md) is `nil`, in macOS 10.6 and later, [`clickedPathComponentCell()`](nspathcontrol/clickedpathcomponentcell().md) returns the clicked cell.

## Topics

### Setting the Control Style
- [var pathStyle: NSPathControl.Style](nspathcontrol/pathstyle.md)
  The receiver’s path style.
### Setting the Background Color
- [var backgroundColor: NSColor?](nspathcontrol/backgroundcolor.md)
  The receiver’s background color.
### Managing Path Components
- [func clickedPathComponentCell() -> NSPathComponentCell?](nspathcontrol/clickedpathcomponentcell.md)
  Returns the clicked cell.
- [func pathComponentCells() -> [NSPathComponentCell]](nspathcontrol/pathcomponentcells.md)
  Returns an array of the `NSPathComponentCell` objects currently being displayed.
- [func setPathComponentCells([NSPathComponentCell])](nspathcontrol/setpathcomponentcells(_:).md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.
### Setting the Double-Click Action
- [var doubleAction: Selector?](nspathcontrol/doubleaction.md)
  The receiver’s double-click action method.
### Setting the Path
- [var url: URL?](nspathcontrol/url.md)
  The path value displayed by the receiver.
### Setting the Delegate
- [var delegate: (any NSPathControlDelegate)?](nspathcontrol/delegate.md)
  The receiver’s delegate.
### Setting the Drag Operation Mask
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nspathcontrol/setdraggingsourceoperationmask(_:forlocal:).md)
  Configures the default value returned from [`draggingSourceOperationMaskForLocal:`](https://developer.apple.com/documentation/objectivec/nsobject/1415984-draggingsourceoperationmaskforlo).
### Setting Popup Menu
- [var menu: NSMenu?](nspathcontrol/menu.md)
  The menu that is used for the path control’s cells.
### Instance Properties
- [var allowedTypes: [String]?](nspathcontrol/allowedtypes.md)
- [var clickedPathItem: NSPathControlItem?](nspathcontrol/clickedpathitem.md)
- [var isEditable: Bool](nspathcontrol/iseditable.md)
- [var pathItems: [NSPathControlItem]](nspathcontrol/pathitems.md)
- [var placeholderAttributedString: NSAttributedString?](nspathcontrol/placeholderattributedstring.md)
- [var placeholderString: String?](nspathcontrol/placeholderstring.md)
### Enumerations
- [NSPathControl.Style](nspathcontrol/style.md)
  `NSPathStyle` constants represent the different visual and behavioral styles an `NSPathControl` or `NSPathCell` object can have.

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol)*