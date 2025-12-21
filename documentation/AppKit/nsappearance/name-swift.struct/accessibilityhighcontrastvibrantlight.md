# accessibilityHighContrastVibrantLight

**Framework**: AppKit  
**Kind**: property

A high-contrast version of the light vibrant appearance.

**Availability**:
- macOS 10.14+

## Declaration

```swift
static let accessibilityHighContrastVibrantLight: NSAppearance.Name
```

#### Discussion

Don’t assign an [`NSAppearance`](nsappearance.md) object with this type directly to one of your views. Instead, assign a light appearance to your view. AppKit then returns this type when the user enables the Increase Contrast option in the Accessibility system preferences and the view’s [`allowsVibrancy`](nsview/allowsvibrancy.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [static let aqua: NSAppearance.Name](nsappearance/name-swift.struct/aqua.md)
  The standard light system appearance.
- [static let darkAqua: NSAppearance.Name](nsappearance/name-swift.struct/darkaqua.md)
  The standard dark system appearance.
- [static let vibrantLight: NSAppearance.Name](nsappearance/name-swift.struct/vibrantlight.md)
  The light vibrant appearance, available only in visual effect views.
- [static let vibrantDark: NSAppearance.Name](nsappearance/name-swift.struct/vibrantdark.md)
  A dark vibrant appearance, available only in visual effect views.
- [static let accessibilityHighContrastAqua: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastaqua.md)
  A high-contrast version of the standard light system appearance.
- [static let accessibilityHighContrastDarkAqua: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastdarkaqua.md)
  A high-contrast version of the standard dark system appearance.
- [static let accessibilityHighContrastVibrantDark: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastvibrantdark.md)
  A high-contrast version of the dark vibrant appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/name-swift.struct/accessibilityhighcontrastvibrantlight)*