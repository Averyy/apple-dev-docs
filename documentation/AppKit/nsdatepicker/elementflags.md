# NSDatePicker.ElementFlags

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the date and time elements displayed by the picker.

**Availability**:
- macOS

## Declaration

```swift
struct ElementFlags
```

```c
enum NSDatePickerElementFlags : NSUInteger;
```

#### Overview

You can combine these constants using the C bitwise `OR` operator.

## Topics

### Constants
- [static var era: NSDatePicker.ElementFlags](./elementflags/era.md)
- [static var hourMinute: NSDatePicker.ElementFlags](./elementflags/hourminute.md)
- [static var hourMinuteSecond: NSDatePicker.ElementFlags](./elementflags/hourminutesecond.md)
- [static var timeZone: NSDatePicker.ElementFlags](./elementflags/timezone.md)
- [static var yearMonth: NSDatePicker.ElementFlags](./elementflags/yearmonth.md)
- [static var yearMonthDay: NSDatePicker.ElementFlags](./elementflags/yearmonthday.md)
### Initializers
- [init(rawValue: UInt)](./elementflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring Date Pickers
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value that indicates whether the date picker draws a bezeled border.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value that indicates whether the date picker has a plain border.
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The date picker’s background color.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value that indicates whether the date picker draws the background.
- [var textColor: NSColor](./textcolor.md)
  The date picker’s text color.
- [var datePickerStyle: NSDatePicker.Style](./datepickerstyle.md)
  The date picker’s style.
- [var presentsCalendarOverlay: Bool](./presentscalendaroverlay.md)
  A Boolean value that indicates whether to present a graphical calendar overlay when editing a calendar element within a text-field style date picker.
- [var delegate: (any NSDatePickerCellDelegate)?](./delegate.md)
  A delegate for the date picker’s cell
- [var datePickerElements: NSDatePicker.ElementFlags](./datepickerelements.md)
  A bitmask that indicates which visual elements of the date picker are currently shown, and which won’t be usable because they are hidden.
- [NSDatePicker.Style](./style.md)
  Constants that define the visual appearance of the date picker cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/elementflags)*