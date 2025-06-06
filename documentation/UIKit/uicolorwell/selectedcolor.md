# selectedColor

**Framework**: UIKit  
**Kind**: property

The selected color in the color picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedColor: UIColor? { get set }
```

#### Discussion

When a person selects a new color in the color picker, the system generates the control event [`valueChanged`](uicontrol/event/valuechanged.md).

This property is KVO-compliant.

## See Also

- [var title: String?](uicolorwell/title.md)
  The title for the color picker.
- [var supportsAlpha: Bool](uicolorwell/supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorwell/selectedcolor)*