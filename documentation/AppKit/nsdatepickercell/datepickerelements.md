# datePickerElements

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A bitmask that indicates which visual elements are shown by the date picker.

**Availability**:
- macOS

## Declaration

```swift
var datePickerElements: NSDatePicker.ElementFlags { get set }
```

```objc
@property NSDatePickerElementFlags datePickerElements;
```

#### Discussion

Elements not included in the bitmask are hidden from view. For a list of possible values, see [`NSDatePicker.ElementFlags`](../nsdatepicker/elementflags.md).

## See Also

### Configuring Appearance
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The cell’s background color.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value indicating whether the cell draws its background.
- [var textColor: NSColor](./textcolor.md)
  The cell’s text color.
- [var datePickerStyle: NSDatePicker.Style](./datepickerstyle.md)
  The date picker style to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/datepickerelements)*