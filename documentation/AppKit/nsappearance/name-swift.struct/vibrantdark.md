# vibrantDark

**Framework**: AppKit  
**Kind**: property

A dark vibrant appearance, available only in visual effect views.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static let vibrantDark: NSAppearance.Name
```

#### Discussion

Vibrant appearances use color blending to make the foreground appearance stand out from the background more prominently.

Don’t assign an [`NSAppearance`](nsappearance.md) object with this type directly to one of your views. Instead, assign a dark appearance to your view, make sure its [`allowsVibrancy`](nsview/allowsvibrancy.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true), and embed the view in a visual effect view. When you do, AppKit updates your view’s appearance to this type.

## See Also

- [static let aqua: NSAppearance.Name](nsappearance/name-swift.struct/aqua.md)
  The standard light system appearance.
- [static let darkAqua: NSAppearance.Name](nsappearance/name-swift.struct/darkaqua.md)
  The standard dark system appearance.
- [static let vibrantLight: NSAppearance.Name](nsappearance/name-swift.struct/vibrantlight.md)
  The light vibrant appearance, available only in visual effect views.
- [static let accessibilityHighContrastAqua: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastaqua.md)
  A high-contrast version of the standard light system appearance.
- [static let accessibilityHighContrastDarkAqua: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastdarkaqua.md)
  A high-contrast version of the standard dark system appearance.
- [static let accessibilityHighContrastVibrantLight: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastvibrantlight.md)
  A high-contrast version of the light vibrant appearance.
- [static let accessibilityHighContrastVibrantDark: NSAppearance.Name](nsappearance/name-swift.struct/accessibilityhighcontrastvibrantdark.md)
  A high-contrast version of the dark vibrant appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance/name-swift.struct/vibrantdark)*