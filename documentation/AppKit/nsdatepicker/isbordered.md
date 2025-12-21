# isBordered

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the date picker has a plain border.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isBordered: Bool { get set }
```

#### Discussion

This property contains [`true`](https://developer.apple.com/documentation/Swift/true) if the date picker has a plain boarder; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isBezeled: Bool](nsdatepicker/isbezeled.md)
  A Boolean value that indicates whether the date picker draws a bezeled border.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/isbordered)*