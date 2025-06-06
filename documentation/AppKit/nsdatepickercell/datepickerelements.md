# datePickerElements

**Framework**: AppKit  
**Kind**: property

A bitmask that indicates which visual elements are shown by the date picker.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var datePickerElements: NSDatePicker.ElementFlags { get set }
```

#### Discussion

Elements not included in the bitmask are hidden from view. For a list of possible values, see [`NSDatePicker.ElementFlags`](nsdatepicker/elementflags.md).

## See Also

- [var backgroundColor: NSColor](nsdatepickercell/backgroundcolor.md)
  The cell’s background color.
- [var drawsBackground: Bool](nsdatepickercell/drawsbackground.md)
  A Boolean value indicating whether the cell draws its background.
- [var textColor: NSColor](nsdatepickercell/textcolor.md)
  The cell’s text color.
- [var datePickerStyle: NSDatePicker.Style](nsdatepickercell/datepickerstyle.md)
  The date picker style to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/datepickerelements)*