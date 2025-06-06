# colorList

**Framework**: AppKit  
**Kind**: property

The list of colors displayed in the color picker.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var colorList: NSColorList! { get set }
```

#### Discussion

Defaults to the standard system color list.

Note that setting a custom color list disables the additional tints and shades that appear when the user sustains a touch.

## See Also

- [var allowedColorSpaces: [NSColorSpace]?](nscolorpickertouchbaritem/allowedcolorspaces.md)
  Controls the color spaces that the color picker can produce.
- [var showsAlpha: Bool](nscolorpickertouchbaritem/showsalpha.md)
  A Boolean value that controls whether the color picker allows picking of colors with alpha values other than `1.0`.
- [var isEnabled: Bool](nscolorpickertouchbaritem/isenabled.md)
  A Boolean value that determines whether the color picker is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/colorlist)*