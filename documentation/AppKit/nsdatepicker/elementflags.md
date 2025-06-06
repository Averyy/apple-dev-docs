# NSDatePicker.ElementFlags

**Framework**: AppKit  
**Kind**: struct

Constants that specify the date and time elements displayed by the picker.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ElementFlags
```

#### Overview

You can combine these constants using the C bitwise `OR` operator.

## Topics

### Constants
- [static var era: NSDatePicker.ElementFlags](nsdatepicker/elementflags/era.md)
- [static var hourMinute: NSDatePicker.ElementFlags](nsdatepicker/elementflags/hourminute.md)
- [static var hourMinuteSecond: NSDatePicker.ElementFlags](nsdatepicker/elementflags/hourminutesecond.md)
- [static var timeZone: NSDatePicker.ElementFlags](nsdatepicker/elementflags/timezone.md)
- [static var yearMonth: NSDatePicker.ElementFlags](nsdatepicker/elementflags/yearmonth.md)
- [static var yearMonthDay: NSDatePicker.ElementFlags](nsdatepicker/elementflags/yearmonthday.md)
### Initializers
- [init(rawValue: UInt)](nsdatepicker/elementflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

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
- [NSDatePicker.Style](nsdatepicker/style.md)
  Constants that define the visual appearance of the date picker cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/elementflags)*