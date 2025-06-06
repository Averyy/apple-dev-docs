# ignoresAlpha

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the app supports alpha.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class var ignoresAlpha: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the app doesn’t support alpha; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The system consults this global value when the app imports alpha (for instance, through color dragging). By default this property is [`false`](https://developer.apple.com/documentation/swift/false); meaning the system supports the alpha component for colors globally. To ignore alpha for an app, invoke the `setIgnoresAlpha` method with a parameter of [`true`](https://developer.apple.com/documentation/swift/true). This value also determines whether the color panel has an opacity slider.

This method provides a global approach for removing alpha, which might not always be appropriate. Apps that need to disable alpha can use more fine-grained APIs for individual controls, such as [`showsAlpha`](nscolorpanel/showsalpha.md) and [`supportsAlpha`](nscolorwell/supportsalpha.md).

In macOS 13 and earlier, the default value is [`true`](https://developer.apple.com/documentation/swift/true). This property is deprecated as of macOS 14.

## See Also

- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/ignoresalpha)*