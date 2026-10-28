# presentsCalendarOverlay

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to present a graphical calendar overlay when editing a calendar element within a text-field style date picker.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
var presentsCalendarOverlay: Bool { get set }
```

```objc
@property BOOL presentsCalendarOverlay;
```

## Discussion

The default value is `NO`. The overlay only appears for text-style date pickers when you select a calendar element. The overlay doesn’t appear when there are no calendar events or the value of this property is `YES`.

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
- [var delegate: (any NSDatePickerCellDelegate)?](./delegate.md)
  A delegate for the date picker’s cell
- [var datePickerElements: NSDatePicker.ElementFlags](./datepickerelements.md)
  A bitmask that indicates which visual elements of the date picker are currently shown, and which won’t be usable because they are hidden.
- [NSDatePicker.ElementFlags](./elementflags.md)
  Constants that specify the date and time elements displayed by the picker.
- [NSDatePicker.Style](./style.md)
  Constants that define the visual appearance of the date picker cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/presentscalendaroverlay)*