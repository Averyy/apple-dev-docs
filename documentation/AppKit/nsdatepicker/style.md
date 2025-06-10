# NSDatePicker.Style

**Framework**: AppKit  
**Kind**: enum

Constants that define the visual appearance of the date picker cell.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Style
```

## Topics

### Enumeration Cases
- [NSDatePicker.Style.clockAndCalendar](nsdatepicker/style/clockandcalendar.md)
- [NSDatePicker.Style.textField](nsdatepicker/style/textfield.md)
- [NSDatePicker.Style.textFieldAndStepper](nsdatepicker/style/textfieldandstepper.md)
### Initializers
- [init?(rawValue: UInt)](nsdatepicker/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [NSDatePicker.ElementFlags](nsdatepicker/elementflags.md)
  Constants that specify the date and time elements displayed by the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/style)*