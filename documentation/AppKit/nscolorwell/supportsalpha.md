# supportsAlpha

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the color picker supports alpha values.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
var supportsAlpha: Bool { get set }
```

#### Discussion

If this property is [`false`](https://developer.apple.com/documentation/Swift/false), people can select only fully opaque colors from the color picker. A value of [`false`](https://developer.apple.com/documentation/Swift/false) also hides the alpha slider. Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) enables partial color opacity, and also makes the alpha slider visible.

If [`ignoresAlpha`](nscolor/ignoresalpha.md) is [`true`](https://developer.apple.com/documentation/Swift/true), this property always returns [`false`](https://developer.apple.com/documentation/Swift/false), disabling alpha globally.

By default this value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var color: NSColor](nscolorwell/color.md)
  The currently selected color for the color well.
- [func takeColorFrom(Any?)](nscolorwell/takecolorfrom(_:).md)
  Changes the currently selected color to the color of the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/supportsalpha)*