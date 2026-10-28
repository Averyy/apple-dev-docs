# ignoresAlpha

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the app supports alpha.

**Availability**:
- macOS 10.0+ - Deprecated in 14.0

> **Deprecated**: Use [`showsAlpha`](../nscolorpanel/showsalpha.md) and [`supportsAlpha`](../nscolorwell/supportsalpha.md) to manage alpha behavior for individual controls.

## Declaration

```swift
@MainActor
class var ignoresAlpha: Bool { get set }
```

```objc
@property (class) BOOL ignoresAlpha;
```

## Return Value

[`true`](../../Swift/true.md) if the app doesn’t support alpha; otherwise, [`false`](../../Swift/false.md).

## Discussion

The system consults this global value when the app imports alpha (for instance, through color dragging). By default this property is [`false`](../../Swift/false.md); meaning the system supports the alpha component for colors globally. To ignore alpha for an app, invoke the `setIgnoresAlpha` method with a parameter of [`true`](../../Swift/true.md). This value also determines whether the color panel has an opacity slider.

This method provides a global approach for removing alpha, which might not always be appropriate. Apps that need to disable alpha can use more fine-grained APIs for individual controls, such as [`showsAlpha`](../nscolorpanel/showsalpha.md) and [`supportsAlpha`](../nscolorwell/supportsalpha.md).

In macOS 13 and earlier, the default value is [`true`](../../Swift/true.md). This property is deprecated as of macOS 14.

## See Also

### Related Documentation
- [var alphaComponent: CGFloat](./alphacomponent.md)
  The alpha (opacity) component value of the color.
### Deprecated properties
- [var colorSpaceName: NSColorSpaceName](./colorspacename.md)
  The name of the color space associated with the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/ignoresalpha)*