# NSActionCell

**Framework**: AppKit  
**Kind**: class

An active area inside a control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSActionCell
```

#### Overview

An [`NSActionCell`](nsactioncell.md) does three things: it displays text or an icon; it provides the target object and action method used by its [`NSControl`](nscontrol.md) object; and it handles mouse (cursor) tracking by properly highlighting its area and sending action messages to its target based on cursor movement.

The [`controlView`](nscell/controlview.md) of an [`NSActionCell`](nsactioncell.md) is the view in which the receiver was last drawn.

##### Obtaining and Setting Cell Values

The [`floatValue`](nscell/floatvalue.md), [`intValue`](nscell/intvalue.md), and [`integerValue`](nscell/integervalue.md) methods return the value with their corresponding types after validating any editing of cell content. If the cell is not a text-type cell or the cell value is not scannable to the appropriate type, these return 0.

The [`stringValue`](nscell/stringvalue.md) method returns the receiver’s value as a string object as converted by the cell’s formatter, if one exists. If no formatter exists and the value is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), returns the value as a plain, attributed, or localized formatted string. If the value is not an `NSString` or cannot be converted to one, returns an empty string. The method supplements the [`NSCell`](nscell.md) implementation by validating and retaining any editing changes being made to cell text.

Calling `setObjectValue:` discards any editing of the receiver’s text and sets its object value to the specified object. After doing so, if the object value is different from what it was before the method was invoked, the method marks the receiver as needing redisplay.

##### Configuring an Nsactioncell Object

The `NSActionCell` implementation of [`setFloatingPointFormat:left:right:`](nscell/setfloatingpointformat:left:right:.md) supplements the `NSCell` implementation by marking the receiver as needing redisplay after discarding any editing changes that were being made to cell text.

## Topics

### Assigning the Target and Action
- [var action: Selector?](nsactioncell/action.md)
  Returns the receiver’s action-message selector.
- [var target: AnyObject?](nsactioncell/target.md)
  Returns the receiver’s target object.
### Assigning a Tag
- [var tag: Int](nsactioncell/tag.md)
  Returns the receiver’s tag.

## Relationships

### Inherits From
- [NSCell](nscell.md)
### Inherited By
- [NSButtonCell](nsbuttoncell.md)
- [NSDatePickerCell](nsdatepickercell.md)
- [NSFormCell](nsformcell.md)
- [NSLevelIndicatorCell](nslevelindicatorcell.md)
- [NSPathCell](nspathcell.md)
- [NSSegmentedCell](nssegmentedcell.md)
- [NSSliderCell](nsslidercell.md)
- [NSStepperCell](nssteppercell.md)
- [NSTextFieldCell](nstextfieldcell.md)
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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)

## See Also

- [class NSView](nsview.md)
  The infrastructure for drawing, printing, and handling events in an app.
- [class NSControl](nscontrol.md)
  A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.
- [class NSCell](nscell.md)
  A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](nsview.md) subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsactioncell)*