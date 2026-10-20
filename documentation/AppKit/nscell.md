# NSCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](./nsview.md) subclass.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
class NSCell
```

```objc
@interface NSCell : NSObject
```

#### Overview

Cells are used by most of the [`NSControl`](./nscontrol.md) classes to implement their internal workings.

##### Designated Initializers

When subclassing `NSCell` you must implement all of the designated initializers. Those methods include [`init()`](./nscell/init%28%29.md), [`init(coder:)`](./nscell/init%28coder%29.md), [`init(textCell:)`](./nscell/init%28textcell%29.md), and [`init(imageCell:)`](./nscell/init%28imagecell%29.md).

## Topics

### Initializing a Cell
- [init(imageCell: NSImage?)](./nscell/init%28imagecell%29.md)
  Returns an `NSCell` object initialized with the specified image and set to have the cell’s default menu.
- [init(textCell: String)](./nscell/init%28textcell%29.md)
  Returns an NSCell object initialized with the specified string and set to have the cell’s default menu.
### Managing Cell Values
- [var objectValue: Any?](./nscell/objectvalue.md)
  The cell’s value as an Objective-C object.
- [var hasValidObjectValue: Bool](./nscell/hasvalidobjectvalue.md)
  A Boolean value that indicates whether the cell has a valid object value.
- [var intValue: Int32](./nscell/intvalue.md)
  The cell’s value as an integer.
- [var integerValue: Int](./nscell/integervalue.md)
  The cell’s value as an integer value.
- [var stringValue: String](./nscell/stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](./nscell/doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](./nscell/floatvalue.md)
  The cell’s value as a single-precision floating-point number.
### Managing Cell Attributes
- [func setCellAttribute(NSCell.Attribute, to: Int)](./nscell/setcellattribute%28_,to%29.md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](./nscell/cellattribute%28_%29.md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](./nscell/type.md)
  The type of the cell.
- [var isEnabled: Bool](./nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](./nscell/allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.
### Managing Display Attributes
- [var isBezeled: Bool](./nscell/isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](./nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](./nscell/isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var backgroundStyle: NSView.BackgroundStyle](./nscell/backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./nscell/interiorbackgroundstyle.md)
  The cell’s interior background style.
- [NSView.BackgroundStyle](./nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
### Managing Cell State
- [var allowsMixedState: Bool](./nscell/allowsmixedstate.md)
  A Boolean value indicating whether the cell supports three states instead of two.
- [var nextState: Int](./nscell/nextstate.md)
  The cell’s next state.
- [func setNextState()](./nscell/setnextstate%28%29.md)
  Changes cell’s state to the next value in the sequence.
- [var state: NSControl.StateValue](./nscell/state.md)
  The cell’s current state.
- [NSControl.StateValue](./nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.
### Modifying Textual Attributes
- [var isEditable: Bool](./nscell/iseditable.md)
  A Boolean value indicating whether the cell is editable.
- [var isSelectable: Bool](./nscell/isselectable.md)
  A Boolean value indicating whether the cell’s text can be selected.
- [var isScrollable: Bool](./nscell/isscrollable.md)
  A Boolean value indicating whether excess text scrolls past the cell’s bounds.
- [var alignment: NSTextAlignment](./nscell/alignment.md)
  The alignment of the cell’s text.
- [var font: NSFont?](./nscell/font.md)
  The font that the cell uses to display text.
- [var lineBreakMode: NSLineBreakMode](./nscell/linebreakmode.md)
  The line break mode to use when drawing text in the cell.
- [var truncatesLastVisibleLine: Bool](./nscell/truncateslastvisibleline.md)
  A Boolean value indicating whether the cell truncates text that does not fit within the cell’s bounds.
- [var wraps: Bool](./nscell/wraps.md)
  A Boolean value indicating whether the cell wraps text whose length that exceeds the cell’s frame.
- [var baseWritingDirection: NSWritingDirection](./nscell/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.
- [var attributedStringValue: NSAttributedString](./nscell/attributedstringvalue.md)
  The cell’s value as an attributed string.
- [var allowsEditingTextAttributes: Bool](./nscell/allowseditingtextattributes.md)
  A Boolean value indicating whether the cell allows the editing of its content’s text attributes by the user.
- [var importsGraphics: Bool](./nscell/importsgraphics.md)
  A Boolean value indicating whether the cell supports the importation of images into its text.
- [func setUpFieldEditorAttributes(NSText) -> NSText](./nscell/setupfieldeditorattributes%28_%29.md)
  Configures the textual and background attributes of the receiver’s field editor.
- [var title: String](./nscell/title.md)
  The cell’s title text.
### Managing the Target and Action
- [var action: Selector?](./nscell/action.md)
  The action performed by the cell.
- [var target: AnyObject?](./nscell/target.md)
  The object that receives the cell’s action messages.
- [var isContinuous: Bool](./nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./nscell/sendaction%28on%29.md)
  Sets the conditions on which the receiver sends action messages to its target.
### Managing the Image
- [var image: NSImage?](./nscell/image.md)
  The image displayed by the cell, if any.
### Managing the Tag
- [var tag: Int](./nscell/tag.md)
  A tag for identifying the cell.
### Formatting and Validating Data
- [var formatter: Formatter?](./nscell/formatter.md)
  The cell’s formatter object.
### Managing Menus
- [class var defaultMenu: NSMenu?](./nscell/defaultmenu.md)
  Returns the default menu for instances of the cell.
- [var menu: NSMenu?](./nscell/menu.md)
  The cell’s contextual menu.
- [func menu(for: NSEvent, in: NSRect, of: NSView) -> NSMenu?](./nscell/menu%28for,in,of%29.md)
  Returns the menu associated with the cell and related to the specified event and frame.
### Comparing Cells
- [func compare(Any) -> ComparisonResult](./nscell/compare%28_%29.md)
  Compares the string values of the receiver another cell, disregarding case.
### Respond to Keyboard Events
- [var acceptsFirstResponder: Bool](./nscell/acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var showsFirstResponder: Bool](./nscell/showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [var refusesFirstResponder: Bool](./nscell/refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.
- [func performClick(Any?)](./nscell/performclick%28_%29.md)
  Simulates a single mouse click on the receiver.
### Deriving Values
- [func takeObjectValueFrom(Any?)](./nscell/takeobjectvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](./nscell/takeintegervaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntValueFrom(Any?)](./nscell/takeintvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeStringValueFrom(Any?)](./nscell/takestringvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.
- [func takeDoubleValueFrom(Any?)](./nscell/takedoublevaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](./nscell/takefloatvaluefrom%28_%29.md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.
### Representing an Object
- [var representedObject: Any?](./nscell/representedobject.md)
  The object represented by the cell.
### Tracking the Mouse
- [func trackMouse(with: NSEvent, in: NSRect, of: NSView, untilMouseUp: Bool) -> Bool](./nscell/trackmouse%28with,in,of,untilmouseup%29.md)
  Initiates the mouse tracking behavior in a cell.
- [func startTracking(at: NSPoint, in: NSView) -> Bool](./nscell/starttracking%28at,in%29.md)
  Begins tracking mouse events within the receiver.
- [func continueTracking(last: NSPoint, current: NSPoint, in: NSView) -> Bool](./nscell/continuetracking%28last,current,in%29.md)
  Returns a Boolean value that indicates whether mouse tracking should continue in the receiving cell.
- [func stopTracking(last: NSPoint, current: NSPoint, in: NSView, mouseIsUp: Bool)](./nscell/stoptracking%28last,current,in,mouseisup%29.md)
  Stops tracking mouse events within the receiver.
- [var mouseDownFlags: Int](./nscell/mousedownflags.md)
  The modifier flags for the last (left) mouse-down event.
- [class var prefersTrackingUntilMouseUp: Bool](./nscell/preferstrackinguntilmouseup.md)
  Returns a Boolean value that indicates whether tracking stops when the cursor leaves the cell.
- [func getPeriodicDelay(UnsafeMutablePointer<Float>, interval: UnsafeMutablePointer<Float>)](./nscell/getperiodicdelay%28_,interval%29.md)
  Returns the initial delay and repeat values for continuous sending of action messages to target objects.
### Hit Testing
- [func hitTest(for: NSEvent, in: NSRect, of: NSView) -> NSCell.HitResult](./nscell/hittest%28for,in,of%29.md)
  Returns hit testing information for the receiver.
### Managing the Cursor
- [func resetCursorRect(NSRect, in: NSView)](./nscell/resetcursorrect%28_,in%29.md)
  Sets the receiver to show the I-beam cursor while it tracks the mouse.
### Handling Keyboard Alternatives
- [var keyEquivalent: String](./nscell/keyequivalent.md)
  The key equivalent associated with clicking the cell.
### Dragging Cells
- [func draggingImageComponents(withFrame: NSRect, in: NSView) -> [NSDraggingImageComponent]](./nscell/draggingimagecomponents%28withframe,in%29.md)
  Generates dragging image components with the specified frame in the view.
### Managing Focus Rings
- [func drawFocusRingMask(withFrame: NSRect, in: NSView)](./nscell/drawfocusringmask%28withframe,in%29.md)
  Draws the focus ring for the control.
- [func focusRingMaskBounds(forFrame: NSRect, in: NSView) -> NSRect](./nscell/focusringmaskbounds%28forframe,in%29.md)
  Returns the bounds of the focus ring mask.
- [class var defaultFocusRingType: NSFocusRingType](./nscell/defaultfocusringtype.md)
  Returns the default type of focus ring for the receiver.
- [var focusRingType: NSFocusRingType](./nscell/focusringtype.md)
  The type of focus ring to use with the associated view.
### Determining Cell Size
- [func calcDrawInfo(NSRect)](./nscell/calcdrawinfo%28_%29.md)
  Recalculates the cell geometry.
- [var cellSize: NSSize](./nscell/cellsize.md)
  The minimum size needed to display the cell.
- [func cellSize(forBounds: NSRect) -> NSSize](./nscell/cellsize%28forbounds%29.md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func drawingRect(forBounds: NSRect) -> NSRect](./nscell/drawingrect%28forbounds%29.md)
  Returns the rectangle within which the receiver draws itself
- [func imageRect(forBounds: NSRect) -> NSRect](./nscell/imagerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its image.
- [func titleRect(forBounds: NSRect) -> NSRect](./nscell/titlerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](./nscell/controlsize.md)
  The size of the cell.
### Drawing and Highlighting
- [func draw(withFrame: NSRect, in: NSView)](./nscell/draw%28withframe,in%29.md)
  Draws the receiver’s border and then draws the interior of the cell.
- [func highlightColor(withFrame: NSRect, in: NSView) -> NSColor?](./nscell/highlightcolor%28withframe,in%29.md)
  Returns the color the receiver uses when drawing the selection highlight.
- [func drawInterior(withFrame: NSRect, in: NSView)](./nscell/drawinterior%28withframe,in%29.md)
  Draws the interior portion of the receiver, which includes the image or text portion but does not include the border.
- [var controlView: NSView?](./nscell/controlview.md)
  The view associated with the cell.
- [func highlight(Bool, withFrame: NSRect, in: NSView)](./nscell/highlight%28_,withframe,in%29.md)
  Redraws the receiver with the specified highlight setting.
- [var isHighlighted: Bool](./nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.
### Editing and Selecting Text
- [func edit(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, event: NSEvent?)](./nscell/edit%28withframe,in,editor,delegate,event%29.md)
  Begins editing of the receiver’s text using the specified field editor.
- [func select(withFrame: NSRect, in: NSView, editor: NSText, delegate: Any?, start: Int, length: Int)](./nscell/select%28withframe,in,editor,delegate,start,length%29.md)
  Selects the specified text range in the cell’s field editor.
- [var sendsActionOnEndEditing: Bool](./nscell/sendsactiononendediting.md)
  A Boolean value indicating whether the cell’s control object sends its action message when the user finishes editing the cell’s text.
- [func endEditing(NSText)](./nscell/endediting%28_%29.md)
  Ends the editing of text in the receiver using the specified field editor.
- [var wantsNotificationForMarkedText: Bool](./nscell/wantsnotificationformarkedtext.md)
  A Boolean value indicating whether the cell’s field editor should post text change notifications.
- [func fieldEditor(for: NSView) -> NSTextView?](./nscell/fieldeditor%28for%29.md)
  Returns a custom field editor for editing in the view.
- [var usesSingleLineMode: Bool](./nscell/usessinglelinemode.md)
  A Boolean value indicating whether the cell restricts layout and rendering of text to a single line.
### Managing Expansion Frames
- [func expansionFrame(withFrame: NSRect, in: NSView) -> NSRect](./nscell/expansionframe%28withframe,in%29.md)
  Returns the expansion cell frame for the receiver.
- [func draw(withExpansionFrame: NSRect, in: NSView)](./nscell/draw%28withexpansionframe,in%29.md)
  Instructs the receiver to draw in an expansion frame.
### User Interface Layout Direction
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](./nscell/userinterfacelayoutdirection.md)
  The layout direction of the user interface.
### Constants
- [NSCell.CellType](./nscell/celltype.md)
  Constants for specifying how a cell represents its data (as text or as an image).
- [NSCell.Attribute](./nscell/attribute.md)
  Constants for specifying how a button behaves when pressed and how it displays its state.
- [NSControl.ImagePosition](./nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [enum NSImageScaling](./nsimagescaling.md)
  Constants that specify a cell’s image scaling behavior.
- [NSCell.StyleMask](./nscell/stylemask.md)
  Constants for specifying what happens when a button is pressed or is displaying its alternate state.
- [enum NSControlTint](./nscontroltint.md)
  Constants for specifying a cell’s tint color.
- [NSControl.ControlSize](./nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [NSCell.HitResult](./nscell/hitresult.md)
  Constants used by the [`hitTest(for:in:of:)`](./nscell/hittest%28for,in,of%29.md) method to determine the effect of an event.
- [NSView.BackgroundStyle](./nsview/backgroundstyle.md)
  Background styles to apply to a view’s cell.
- [Deprecated Scaling Constants](./deprecated-scaling-constants.md)
  These are deprecated scaling constants.
- [Data Entry Types](./data-entry-types.md)
  These constants specify how a cell formats numeric data.
### Initializers
- [init()](./nscell/init%28%29.md)
- [init(coder: NSCoder)](./nscell/init%28coder%29.md)
### Deprecated
- [Deprecated symbols](./nscell-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSActionCell](./nsactioncell.md)
- [NSBrowserCell](./nsbrowsercell.md)
- [NSImageCell](./nsimagecell.md)
- [NSTextAttachmentCell](./nstextattachmentcell-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)

## See Also

### View fundamentals
- [class NSView](./nsview.md)
  The infrastructure for drawing, printing, and handling events in an app.
- [class NSControl](./nscontrol.md)
  A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.
- [class NSActionCell](./nsactioncell.md)
  An active area inside a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell)*