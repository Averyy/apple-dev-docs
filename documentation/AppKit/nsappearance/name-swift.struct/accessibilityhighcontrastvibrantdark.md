# accessibilityHighContrastVibrantDark

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A high-contrast version of the dark vibrant appearance.

**Availability**:
- macOS 10.14+

## Declaration

```swift
static let accessibilityHighContrastVibrantDark: NSAppearance.Name
```

```c
extern NSAppearanceName const NSAppearanceNameAccessibilityHighContrastVibrantDark;
```

#### Discussion

Don’t assign an [`NSAppearance`](../../nsappearance.md) object with this type directly to one of your views. Instead, assign a dark appearance to your view. AppKit then returns this type when the user enables the Increase Contrast option in the Accessibility system preferences and the view’s [`allowsVibrancy`](../../nsview/allowsvibrancy.md) property is [`true`](../../../Swift/true.md).

## See Also

### System Appearance Names
- [static let aqua: NSAppearance.Name](./aqua.md)
  The standard light system appearance.
- [static let darkAqua: NSAppearance.Name](./darkaqua.md)
  The standard dark system appearance.
- [static let vibrantLight: NSAppearance.Name](./vibrantlight.md)
  The light vibrant appearance, available only in visual effect views.
- [static let vibrantDark: NSAppearance.Name](./vibrantdark.md)
  A dark vibrant appearance, available only in visual effect views.
- [static let accessibilityHighContrastAqua: NSAppearance.Name](./accessibilityhighcontrastaqua.md)
  A high-contrast version of the standard light system appearance.
- [static let accessibilityHighContrastDarkAqua: NSAppearance.Name](./accessibilityhighcontrastdarkaqua.md)
  A high-contrast version of the standard dark system appearance.
- [static let accessibilityHighContrastVibrantLight: NSAppearance.Name](./accessibilityhighcontrastvibrantlight.md)
  A high-contrast version of the light vibrant appearance.
- [static let lightContent: NSAppearance.Name](./lightcontent.md)
  The standard appearance that can be used by controls in light content areas (not including window-frame areas).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/name-swift.struct/accessibilityhighcontrastvibrantdark)*