# vibrantLight

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The light vibrant appearance, available only in visual effect views.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static let vibrantLight: NSAppearance.Name
```

```c
extern NSAppearanceName const NSAppearanceNameVibrantLight;
```

#### Discussion

Vibrant appearances use color blending to make the foreground appearance stand out from the background more prominently.

Don’t assign an [`NSAppearance`](../../nsappearance.md) object with this type directly to one of your views. Instead, assign a light appearance to your view, make sure its [`allowsVibrancy`](../../nsview/allowsvibrancy.md) property is set to [`true`](../../../Swift/true.md), and embed the view in a visual effect view. When you do, AppKit updates your view’s appearance to this type.

## See Also

### System Appearance Names
- [static let aqua: NSAppearance.Name](./aqua.md)
  The standard light system appearance.
- [static let darkAqua: NSAppearance.Name](./darkaqua.md)
  The standard dark system appearance.
- [static let vibrantDark: NSAppearance.Name](./vibrantdark.md)
  A dark vibrant appearance, available only in visual effect views.
- [static let accessibilityHighContrastAqua: NSAppearance.Name](./accessibilityhighcontrastaqua.md)
  A high-contrast version of the standard light system appearance.
- [static let accessibilityHighContrastDarkAqua: NSAppearance.Name](./accessibilityhighcontrastdarkaqua.md)
  A high-contrast version of the standard dark system appearance.
- [static let accessibilityHighContrastVibrantLight: NSAppearance.Name](./accessibilityhighcontrastvibrantlight.md)
  A high-contrast version of the light vibrant appearance.
- [static let accessibilityHighContrastVibrantDark: NSAppearance.Name](./accessibilityhighcontrastvibrantdark.md)
  A high-contrast version of the dark vibrant appearance.
- [static let lightContent: NSAppearance.Name](./lightcontent.md)
  The standard appearance that can be used by controls in light content areas (not including window-frame areas).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/name-swift.struct/vibrantlight)*