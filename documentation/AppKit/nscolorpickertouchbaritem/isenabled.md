# isEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the color picker is enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

## Discussion

If the picker is currently displayed as a popover, and you set the value of this property to [`false`](../../Swift/false.md), the picker is dismissed.

## See Also

### Configuring the color picker
- [var colorList: NSColorList!](./colorlist.md)
  The list of colors displayed in the color picker.
- [var allowedColorSpaces: [NSColorSpace]?](./allowedcolorspaces.md)
  Controls the color spaces that the color picker can produce.
- [var showsAlpha: Bool](./showsalpha.md)
  A Boolean value that controls whether the color picker allows picking of colors with alpha values other than `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/isenabled)*