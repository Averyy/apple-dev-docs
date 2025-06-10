# NSDatePicker

**Framework**: AppKit  
**Kind**: class

A display of a calendar date with controls for editing the date value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSDatePicker
```

#### Overview

`NSDatePicker` uses an [`NSDatePickerCell`](nsdatepickercell.md) to implement much of the control’s functionality. `NSDatePicker` provides cover methods for most of `NSDatePickerCell` methods, which invoke the corresponding cell method.

## Topics

### Configuring Date Pickers
- [var isBezeled: Bool](nsdatepicker/isbezeled.md)
  A Boolean value that indicates whether the date picker draws a bezeled border.
- [var isBordered: Bool](nsdatepicker/isbordered.md)
  A Boolean value that indicates whether the date picker has a plain border.
- [var backgroundColor: NSColor](nsdatepicker/backgroundcolor.md)
  The date picker’s background color.
- [var drawsBackground: Bool](nsdatepicker/drawsbackground.md)
  A Boolean value that indicates whether the date picker draws the background.
- [var textColor: NSColor](nsdatepicker/textcolor.md)
  The date picker’s text color.
- [var datePickerStyle: NSDatePicker.Style](nsdatepicker/datepickerstyle.md)
  The date picker’s style.
- [var presentsCalendarOverlay: Bool](nsdatepicker/presentscalendaroverlay.md)
  A Boolean value that indicates whether to present a graphical calendar overlay when editing a calendar element within a text-field style date picker.
- [var delegate: (any NSDatePickerCellDelegate)?](nsdatepicker/delegate.md)
  A delegate for the date picker’s cell
- [var datePickerElements: NSDatePicker.ElementFlags](nsdatepicker/datepickerelements.md)
  A bitmask that indicates which visual elements of the date picker are currently shown, and which won’t be usable because they are hidden.
- [NSDatePicker.ElementFlags](nsdatepicker/elementflags.md)
  Constants that specify the date and time elements displayed by the picker.
- [NSDatePicker.Style](nsdatepicker/style.md)
  Constants that define the visual appearance of the date picker cell.
### Controlling Date Picker Range and Mode
- [var calendar: Calendar?](nsdatepicker/calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](nsdatepicker/locale.md)
  The date picker’s locale.
- [var datePickerMode: NSDatePicker.Mode](nsdatepicker/datepickermode.md)
  The date picker’s mode.
- [var timeZone: TimeZone?](nsdatepicker/timezone.md)
  The time zone for the date picker.
- [NSDatePicker.Mode](nsdatepicker/mode.md)
  Constants that define whether the picker provides a single date, or a range of dates.
### Accessing Object Values
- [var dateValue: Date](nsdatepicker/datevalue.md)
  The date selected by the date picker.
- [var timeInterval: TimeInterval](nsdatepicker/timeinterval.md)
  The time interval selected by the date picker.
### Constraining the Displayable/Selectable Range
- [var minDate: Date?](nsdatepicker/mindate.md)
  The date picker’s minimum date value.
- [var maxDate: Date?](nsdatepicker/maxdate.md)
  The date picker’s maximum date value.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker)*