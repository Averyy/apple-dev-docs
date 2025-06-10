# NSDatePickerCell

**Framework**: AppKit  
**Kind**: class

An object that controls the behavior of a date picker, or of a single date picker cell in a matrix.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSDatePickerCell
```

## Topics

### Configuring Appearance
- [var backgroundColor: NSColor](nsdatepickercell/backgroundcolor.md)
  The cell’s background color.
- [var drawsBackground: Bool](nsdatepickercell/drawsbackground.md)
  A Boolean value indicating whether the cell draws its background.
- [var textColor: NSColor](nsdatepickercell/textcolor.md)
  The cell’s text color.
- [var datePickerStyle: NSDatePicker.Style](nsdatepickercell/datepickerstyle.md)
  The date picker style to use.
- [var datePickerElements: NSDatePicker.ElementFlags](nsdatepickercell/datepickerelements.md)
  A bitmask that indicates which visual elements are shown by the date picker.
### Range Mode
- [var datePickerMode: NSDatePicker.Mode](nsdatepickercell/datepickermode.md)
  The mode in use by the date picker.
### Object Values
- [var dateValue: Date](nsdatepickercell/datevalue.md)
  The date currently specified in the picker.
- [var timeInterval: TimeInterval](nsdatepickercell/timeinterval.md)
  The time interval that represents the date range.
- [var calendar: Calendar?](nsdatepickercell/calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](nsdatepickercell/locale.md)
  The locale used to display dates.
- [var timeZone: TimeZone?](nsdatepickercell/timezone.md)
  The time zone used to display time-related values.
### Date Range Constraints
- [var minDate: Date?](nsdatepickercell/mindate.md)
  The minimum date that the picker allows as input.
- [var maxDate: Date?](nsdatepickercell/maxdate.md)
  The maximum date that the picker allows as input.
### Getting and Setting the Delegate
- [var delegate: (any NSDatePickerCellDelegate)?](nsdatepickercell/delegate.md)
  The delegate associated with the date picker.
### Constants
- [NSDatePicker.Style](nsdatepicker/style.md)
  Constants that define the visual appearance of the date picker cell.
- [NSDatePicker.Mode](nsdatepicker/mode.md)
  Constants that define whether the picker provides a single date, or a range of dates.
- [NSDatePicker.ElementFlags](nsdatepicker/elementflags.md)
  Constants that specify the date and time elements displayed by the picker.
### Initializers
- [init(coder: NSCoder)](nsdatepickercell/init(coder:).md)
- [init(textCell: String)](nsdatepickercell/init(textcell:).md)

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSDatePickerCellDelegate](nsdatepickercelldelegate.md)
  A set of optional methods implemented by delegates of [`NSDatePickerCell`](nsdatepickercell.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell)*