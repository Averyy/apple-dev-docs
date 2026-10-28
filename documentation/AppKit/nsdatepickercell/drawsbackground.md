# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell draws its background.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell draws its background.

## See Also

### Configuring Appearance
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The cell’s background color.
- [var textColor: NSColor](./textcolor.md)
  The cell’s text color.
- [var datePickerStyle: NSDatePicker.Style](./datepickerstyle.md)
  The date picker style to use.
- [var datePickerElements: NSDatePicker.ElementFlags](./datepickerelements.md)
  A bitmask that indicates which visual elements are shown by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/drawsbackground)*