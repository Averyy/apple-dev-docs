# isEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the color picker is enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

If the picker is currently displayed as a popover, and you set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false), the picker is dismissed.

## See Also

- [var colorList: NSColorList!](nscolorpickertouchbaritem/colorlist.md)
  The list of colors displayed in the color picker.
- [var allowedColorSpaces: [NSColorSpace]?](nscolorpickertouchbaritem/allowedcolorspaces.md)
  Controls the color spaces that the color picker can produce.
- [var showsAlpha: Bool](nscolorpickertouchbaritem/showsalpha.md)
  A Boolean value that controls whether the color picker allows picking of colors with alpha values other than `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/isenabled)*