# NSDatePicker.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define the visual appearance of the date picker cell.

**Availability**:
- macOS

## Declaration

```swift
enum Style
```

```c
enum NSDatePickerStyle : NSUInteger;
```

## Topics

### Enumeration Cases
- [NSDatePicker.Style.clockAndCalendar](./style/clockandcalendar.md)
- [NSDatePicker.Style.textField](./style/textfield.md)
- [NSDatePicker.Style.textFieldAndStepper](./style/textfieldandstepper.md)
### Initializers
- [init?(rawValue: UInt)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [NSDatePicker.ElementFlags](./elementflags.md)
  Constants that specify the date and time elements displayed by the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/style)*