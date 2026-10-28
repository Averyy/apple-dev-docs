# isBezeled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the date picker draws a bezeled border.

**Availability**:
- macOS

## Declaration

```swift
var isBezeled: Bool { get set }
```

```objc
@property (getter=isBezeled) BOOL bezeled;
```

## Discussion

This property contains [`true`](../../Swift/true.md) if the date picker has a bezeled boarder; otherwise, [`false`](../../Swift/false.md).

## See Also

### Configuring Date Pickers
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
- [NSDatePicker.Style](./style.md)
  Constants that define the visual appearance of the date picker cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/isbezeled)*