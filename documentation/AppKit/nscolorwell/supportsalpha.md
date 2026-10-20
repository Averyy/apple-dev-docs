# supportsAlpha

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the color picker supports alpha values.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var supportsAlpha: Bool { get set }
```

```objc
@property BOOL supportsAlpha;
```

#### Discussion

If this property is [`false`](../../Swift/false.md), people can select only fully opaque colors from the color picker. A value of [`false`](../../Swift/false.md) also hides the alpha slider. Setting this property to [`true`](../../Swift/true.md) enables partial color opacity, and also makes the alpha slider visible.

If [`ignoresAlpha`](../nscolor/ignoresalpha.md) is [`true`](../../Swift/true.md), this property always returns [`false`](../../Swift/false.md), disabling alpha globally.

By default this value is [`true`](../../Swift/true.md).

## See Also

### Managing the selected color
- [var color: NSColor](./color.md)
  The currently selected color for the color well.
- [func takeColorFrom(Any?)](./takecolorfrom%28_%29.md)
  Changes the currently selected color to the color of the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/supportsalpha)*