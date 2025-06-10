# NSControl

**Framework**: AppKit  
**Kind**: class

A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSControl
```

#### Overview

The [`NSControl`](nscontrol.md) class is abstract and must be subclassed to be used. Although you can subclass it yourself, more often you use one of the subclasses already defined by AppKit. A control draws content on the screen, automatically handles user interactions with that content, and calls the action method of its target object for any significant user interactions.

##### About Delegate Methods

The `NSControl` class provides several delegate methods for its subclasses that allow text editing, such as `NSTextField` and `NSMatrix`. These include: [`controlTextDidBeginEditing:`](https://developer.apple.com/documentation/objectivec/nsobject/1428934-controltextdidbeginediting), [`controlTextDidChange:`](https://developer.apple.com/documentation/objectivec/nsobject/1428982-controltextdidchange), and [`controlTextDidEndEditing:`](https://developer.apple.com/documentation/objectivec/nsobject/1428847-controltextdidendediting).

Note that although `NSControl` defines delegate methods, it doesn’t itself have a delegate. Any subclass that uses these methods must have a delegate and the methods to get and set it. In addition, a formal delegate protocol [`NSControlTextEditingDelegate`](nscontroltexteditingdelegate.md) also defines delegate methods used by control delegates.

## Topics

### Creating a Control
- [init(frame: NSRect)](nscontrol/init(frame:).md)
  Initializes a control with the specified frame rectangle.
- [init?(coder: NSCoder)](nscontrol/init(coder:).md)
  Initializes a control with data in an unarchiver.
### Enabling and Disabling the Control
- [var isEnabled: Bool](nscontrol/isenabled.md)
  A Boolean value that indicates whether the receiver reacts to mouse events.
### Accessing the Control’s Value
- [var doubleValue: Double](nscontrol/doublevalue.md)
  The value of the receiver’s cell as a double-precision floating-point number.
- [var floatValue: Float](nscontrol/floatvalue.md)
  The value of the receiver’s cell as a single-precision floating-point number.
- [var intValue: Int32](nscontrol/intvalue.md)
  The value of the receiver’s cell as an integer.
- [var integerValue: Int](nscontrol/integervalue.md)
  The value of the receiver’s cell as an [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) value.
- [var objectValue: Any?](nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [var stringValue: String](nscontrol/stringvalue.md)
  The value of the receiver’s cell as an `NSString` object.
- [var attributedStringValue: NSAttributedString](nscontrol/attributedstringvalue.md)
  The value of the receiver’s cell as an attributed string.
### Interacting with Other Controls
- [func takeDoubleValueFrom(Any?)](nscontrol/takedoublevaluefrom(_:).md)
  Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](nscontrol/takefloatvaluefrom(_:).md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.
- [func takeIntValueFrom(Any?)](nscontrol/takeintvaluefrom(_:).md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](nscontrol/takeintegervaluefrom(_:).md)
  Sets the value of the receiver’s cell to an [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) value obtained from the specified object.
- [func takeObjectValueFrom(Any?)](nscontrol/takeobjectvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the object value obtained from the specified object.
- [func takeStringValueFrom(Any?)](nscontrol/takestringvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.
### Formatting Text
- [var alignment: NSTextAlignment](nscontrol/alignment.md)
  The alignment mode of the text in the receiver’s cell.
- [var font: NSFont?](nscontrol/font.md)
  The font used to draw text in the receiver’s cell.
- [var lineBreakMode: NSLineBreakMode](nscontrol/linebreakmode.md)
  The line break mode to use for text in the control’s cell.
- [var usesSingleLineMode: Bool](nscontrol/usessinglelinemode.md)
  A Boolean value that indicates whether the text in the control’s cell uses single line mode.
- [var formatter: Formatter?](nscontrol/formatter.md)
  The receiver’s formatter.
- [var baseWritingDirection: NSWritingDirection](nscontrol/basewritingdirection.md)
  The initial writing direction used to determine the actual writing direction for text.
### Managing Expansion Tool Tips
- [func draw(withExpansionFrame: NSRect, in: NSView)](nscontrol/draw(withexpansionframe:in:).md)
  Performs custom expansion tool tip drawing.
- [var allowsExpansionToolTips: Bool](nscontrol/allowsexpansiontooltips.md)
  A Boolean value that indicates whether expansion tool tips are shown when the control is hovered over.
- [func expansionFrame(withFrame: NSRect) -> NSRect](nscontrol/expansionframe(withframe:).md)
  The frame in which a tool tip can be displayed, if needed.
### Managing the Field Editor
- [func abortEditing() -> Bool](nscontrol/abortediting.md)
  Terminates the current editing operation and discards any edited text.
- [func currentEditor() -> NSText?](nscontrol/currenteditor.md)
  Returns the current field editor for the control.
- [func validateEditing()](nscontrol/validateediting.md)
  Validates changes to any user-typed text.
- [func edit(withFrame: NSRect, editor: NSText, delegate: Any?, event: NSEvent)](nscontrol/edit(withframe:editor:delegate:event:).md)
  Begins editing of the receiver’s text using the specified field editor.
- [func endEditing(NSText)](nscontrol/endediting(_:).md)
  Ends the editing of text in the receiver using the specified field editor.
- [func select(withFrame: NSRect, editor: NSText, delegate: Any?, start: Int, length: Int)](nscontrol/select(withframe:editor:delegate:start:length:).md)
  Selects the specified text range in the receiver’s field editor.
### Control-Editing Notifications
- [class let textDidBeginEditingNotification: NSNotification.Name](nscontrol/textdidbegineditingnotification.md)
  Sent when a control with editable cells begins an edit session.
- [class let textDidChangeNotification: NSNotification.Name](nscontrol/textdidchangenotification.md)
  Sent when the text in the receiving control changes.
- [class let textDidEndEditingNotification: NSNotification.Name](nscontrol/textdidendeditingnotification.md)
  Sent when a control with editable cells ends an editing session.
### Resizing the Control
- [var controlSize: NSControl.ControlSize](nscontrol/controlsize-swift.property.md)
  The size of the control.
- [NSControl.ControlSize](nscontrol/controlsize-swift.enum.md)
  A constant for specifying a cell’s size.
- [func sizeThatFits(NSSize) -> NSSize](nscontrol/sizethatfits(_:).md)
  Asks the control to calculate and return the size that best fits the specified size.
- [func sizeToFit()](nscontrol/sizetofit.md)
  Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.
### Displaying a Cell
- [var isHighlighted: Bool](nscontrol/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [NSControl.ImagePosition](nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [NSControl.StateValue](nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.
### Implementing the Target-Action Mechanism
- [var action: Selector?](nscontrol/action.md)
  The default action-message selector associated with the control.
- [var target: AnyObject?](nscontrol/target.md)
  The target object that receives action messages from the cell.
- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func sendAction(Selector?, to: Any?) -> Bool](nscontrol/sendaction(_:to:).md)
  Causes the specified action to be sent to the target.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscontrol/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.
### Accessing Tags
- [var tag: Int](nscontrol/tag.md)
  The tag identifying the receiver (not the tag of the receiver’s cell).
### Activating from the Keyboard
- [func performClick(Any?)](nscontrol/performclick(_:).md)
  Simulates a single mouse click on the receiver.
- [var refusesFirstResponder: Bool](nscontrol/refusesfirstresponder.md)
  A Boolean value indicating whether the receiver refuses the first responder role.
### Tracking the Mouse
- [var ignoresMultiClick: Bool](nscontrol/ignoresmulticlick.md)
  A Boolean value indicating whether the receiver ignores multiple clicks made in rapid succession.
### Supporting Constraint-Based Layout
- [func invalidateIntrinsicContentSize(for: NSCell)](nscontrol/invalidateintrinsiccontentsize(for:).md)
  Notifies the control that the intrinsic content size for its cell is no longer valid.
### Deprecated
- [Deprecated Symbols](nscontrol-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Inherited By
- [NSBrowser](nsbrowser.md)
- [NSButton](nsbutton.md)
- [NSColorWell](nscolorwell.md)
- [NSComboButton](nscombobutton.md)
- [NSDatePicker](nsdatepicker.md)
- [NSImageView](nsimageview.md)
- [NSLevelIndicator](nslevelindicator.md)
- [NSMatrix](nsmatrix.md)
- [NSPathControl](nspathcontrol.md)
- [NSRuleEditor](nsruleeditor.md)
- [NSScroller](nsscroller.md)
- [NSSegmentedControl](nssegmentedcontrol.md)
- [NSSlider](nsslider.md)
- [NSStepper](nsstepper.md)
- [NSSwitch](nsswitch.md)
- [NSTableView](nstableview.md)
- [NSTextField](nstextfield.md)
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

- [class NSView](nsview.md)
  The infrastructure for drawing, printing, and handling events in an app.
- [class NSCell](nscell.md)
  A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](nsview.md) subclass.
- [class NSActionCell](nsactioncell.md)
  An active area inside a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol)*