# supportsAlpha

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the color picker supports alpha values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supportsAlpha: Bool { get set }
```

#### Discussion

If this property is [`false`](https://developer.apple.com/documentation/Swift/false), people can only pick fully opaque colors from the color picker.

## See Also

- [var title: String?](uicolorwell/title.md)
  The title for the color picker.
- [var maximumLinearExposure: CGFloat](uicolorwell/maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color well.
- [var supportsEyedropper: Bool](uicolorwell/supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color well.
- [var selectedColor: UIColor?](uicolorwell/selectedcolor.md)
  The selected color in the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorwell/supportsalpha)*