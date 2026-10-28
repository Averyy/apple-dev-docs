# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A delegate for the date picker’s cell

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSDatePickerCellDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSDatePickerCellDelegate> delegate;
```

## Discussion

The date picker’s [`NSDatePickerCell`](../nsdatepickercell.md) instance handles all delegate methods.

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
- [var datePickerElements: NSDatePicker.ElementFlags](./datepickerelements.md)
  A bitmask that indicates which visual elements of the date picker are currently shown, and which won’t be usable because they are hidden.
- [NSDatePicker.ElementFlags](./elementflags.md)
  Constants that specify the date and time elements displayed by the picker.
- [NSDatePicker.Style](./style.md)
  Constants that define the visual appearance of the date picker cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/delegate)*