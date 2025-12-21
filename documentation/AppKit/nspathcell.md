# NSPathCell

**Framework**: AppKit  
**Kind**: class

The user interface of a path control object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class NSPathCell
```

#### Overview

[`NSPathCell`](nspathcell.md) maintains a collection of [`NSPathComponentCell`](nspathcomponentcell.md) objects that represent a particular path to be displayed to the user.

The path shown can be set with the [`clickedPathComponentCell`](nspathcell/clickedpathcomponentcell.md) method. Doing so removes all displayed `NSPathComponentCell` objects and automatically fills the control with `NSPathComponentCell` objects set to have the appropriate icons, display titles, and `NSURL` values for the particular path component they represent. Alternatively, you can fill the control manually by setting the cell array or directly modifying existing cells.

Both an action and double-click action can be set for the path control. To find out what path component cell was clicked in the action, you can read the value of [`clickedPathComponentCell`](nspathcell/clickedpathcomponentcell.md). When the style is set to [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md), the action is still sent, and the [`clickedPathComponentCell`](nspathcell/clickedpathcomponentcell.md) value for the represented menu item is correctly set. The [`clickedPathComponentCell`](nspathcell/clickedpathcomponentcell.md) value is valid only when the action is being sent. It is also valid when the keyboard is used to invoke the action.

Automatic animated expansion of partially hidden `NSPathComponentCell` objects happens if you correctly call [`mouseEntered(with:)`](nsresponder/mouseentered(with:).md) and [`mouseExited(with:)`](nsresponder/mouseexited(with:).md) for each `NSPathComponentCell` in the `NSPathCell` object. This is not required if the [`pathStyle`](nspathcell/pathstyle.md) is set to [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md), or if you wish to not have the animation.

`NSPathCell` supports several path display styles. [`NSPathControl.Style.standard`](nspathcontrol/style/standard.md) has a light blue background with arrows indicating the path. [`NSPathStyleNavigationBar`](nspathstyle/nspathstylenavigationbar.md) has more defined arrows (chevrons) and looks a little like a segmented button. [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md) looks and works like an [`NSPopUpButton`](nspopupbutton.md) object to display the full path, or, if the cell is editable, select a new path.

If the cell’s [`isEditable`](nscell/iseditable.md) method returns [`true`](https://developer.apple.com/documentation/Swift/true) (the default), you can drag and drop into the cell to change the value. You can constrain what can be dropped using UTIs (Uniform Type Identifiers) with [`allowedTypes`](nspathcell/allowedtypes.md) or the appropriate delegate methods on `NSPathControl`.

If the cell’s [`isSelectable`](nscell/isselectable.md) method returns [`true`](https://developer.apple.com/documentation/Swift/true) (the default), the cell’s contents can automatically be dragged out. The proper UTI, filename, and URL are placed on the pasteboard. You can further control or limit this by using the appropriate delegate methods on `NSPathControl`.

If the cell is editable and has the path style set to [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md), an additional item in the pop-up menu allows selecting another location. By default, an `NSOpenPanel` object is configured based on the allowed types. The `NSOpenPanel` object can be customized with a delegate method.

#### Setting the Control Size

When setting the [`controlSize`](nscell/controlsize.md) property, `NSPathCell` properly respects the control size for the [`NSPathControl.Style.standard`](nspathcontrol/style/standard.md) and [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md) styles. When the control size is set, the new size is propagated to subcells. When the path style is set to [`NSPathStyleNavigationBar`](nspathstyle/nspathstylenavigationbar.md), you cannot change the control size, and it is always set to [`NSSmallControlSize`](nssmallcontrolsize.md). Attempting to change the control size when the path style is [`NSPathStyleNavigationBar`](nspathstyle/nspathstylenavigationbar.md) causes an assertion. Setting the path style to [`NSPathStyleNavigationBar`](nspathstyle/nspathstylenavigationbar.md) forces the control size to be [`NSSmallControlSize`](nssmallcontrolsize.md).

## Topics

### Displaying Hidden Components
- [func mouseEntered(with: NSEvent, frame: NSRect, in: NSView)](nspathcell/mouseentered(with:frame:in:).md)
  Displays the cell component over which the mouse is hovering.
- [func mouseExited(with: NSEvent, frame: NSRect, in: NSView)](nspathcell/mouseexited(with:frame:in:).md)
  Hides the cell component over which the mouse is hovering.
### Setting the Allowed Types
- [var allowedTypes: [String]?](nspathcell/allowedtypes.md)
  Sets the component types allowed in the path when the cell is editable.
### Setting the Control Style
- [var pathStyle: NSPathControl.Style](nspathcell/pathstyle.md)
  Sets the receiver’s path style.
### Setting the Object Value
- [func setObjectValue((any NSCopying)?)](nspathcell/setobjectvalue(_:).md)
  Sets the receiver’s object value.
### Setting Cell Appearance
- [var placeholderAttributedString: NSAttributedString?](nspathcell/placeholderattributedstring.md)
  Sets the value of the placeholder attributed string.
- [var placeholderString: String?](nspathcell/placeholderstring.md)
  Returns the placeholder string.
- [var backgroundColor: NSColor?](nspathcell/backgroundcolor.md)
  Returns the current background color of the receiver.
### Managing Path Components
- [class var pathComponentCellClass: AnyClass](nspathcell/pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](nspathcell/rect(of:withframe:in:).md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](nspathcell/pathcomponentcell(at:withframe:in:).md)
  Returns the cell located at the given point within the given frame of the given view.
- [var clickedPathComponentCell: NSPathComponentCell?](nspathcell/clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.
- [var pathComponentCells: [NSPathComponentCell]](nspathcell/pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.
### Setting the Double-Click Action
- [var doubleAction: Selector?](nspathcell/doubleaction.md)
  Sets the receiver’s double-click action.
### Setting the Path
- [var url: URL?](nspathcell/url.md)
  Returns the path displayed by the receiver.
- [var clickedPathComponentCell: NSPathComponentCell?](nspathcell/clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.
### Setting the Delegate
- [var delegate: (any NSPathCellDelegate)?](nspathcell/delegate.md)
  Sets the receiver’s delegate.
### Constants
- [NSPathControl.Style](nspathcontrol/style.md)
  `NSPathStyle` constants represent the different visual and behavioral styles an `NSPathControl` or `NSPathCell` object can have.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSOpenSavePanelDelegate](nsopensavepaneldelegate.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSPathCellDelegate](nspathcelldelegate.md)
  A set of methods that enable the delegate of a path cell object to customize the Open panel or pop-up menu of a path whose style is set to [`NSPathControl.Style.popUp`](nspathcontrol/style/popup.md).
- [class NSPathComponentCell](nspathcomponentcell.md)
  A component of a path.
- [class NSPathControlItem](nspathcontrolitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell)*