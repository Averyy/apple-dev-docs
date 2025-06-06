# presentsCalendarOverlay

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether to present a graphical calendar overlay when editing a calendar element within a text-field style date picker.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
@MainActor
var presentsCalendarOverlay: Bool { get set }
```

#### Discussion

The default value is `NO`. The overlay only appears for text-style date pickers when you select a calendar element. The overlay doesn’t appear when there are no calendar events or the value of this property is `YES`.

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
- [var delegate: (any NSDatePickerCellDelegate)?](nsdatepicker/delegate.md)
  A delegate for the date picker’s cell
- [var datePickerElements: NSDatePicker.ElementFlags](nsdatepicker/datepickerelements.md)
  A bitmask that indicates which visual elements of the date picker are currently shown, and which won’t be usable because they are hidden.
- [NSDatePicker.ElementFlags](nsdatepicker/elementflags.md)
  Constants that specify the date and time elements displayed by the picker.
- [NSDatePicker.Style](nsdatepicker/style.md)
  Constants that define the visual appearance of the date picker cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/presentscalendaroverlay)*