# allowedColorSpaces

**Framework**: AppKit  
**Kind**: property

Controls the color spaces that the color picker can produce.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
var allowedColorSpaces: [NSColorSpace]? { get set }
```

#### Discussion

If a selected color is outside the allowed color spaces, the picker converts it to the first color space in the array.

Set the value of this property to `nil` to allow all color spaces. An empty array is an invalid value.

## See Also

- [var colorList: NSColorList!](nscolorpickertouchbaritem/colorlist.md)
  The list of colors displayed in the color picker.
- [var showsAlpha: Bool](nscolorpickertouchbaritem/showsalpha.md)
  A Boolean value that controls whether the color picker allows picking of colors with alpha values other than `1.0`.
- [var isEnabled: Bool](nscolorpickertouchbaritem/isenabled.md)
  A Boolean value that determines whether the color picker is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/allowedcolorspaces)*