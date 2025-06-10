# NSButton.GradientType

**Framework**: AppKit  
**Kind**: enum

Specify the gradients used by the [`gradientType`](nsbuttoncell/gradienttype.md) property.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum GradientType
```

## Topics

### Constants
- [NSButton.GradientType.none](nsbutton/gradienttype/none.md)
  There is no gradient, so the button looks flat.
- [NSButton.GradientType.concaveWeak](nsbutton/gradienttype/concaveweak.md)
  The top-left corner is light gray, and the bottom-right corner is dark gray, so the button appears to be pushed in.
- [NSButton.GradientType.concaveStrong](nsbutton/gradienttype/concavestrong.md)
  As with `NSGradientConcaveWeak`, the top-left corner is light gray, and the bottom-right corner is dark gray, but the difference between the grays is greater, so the appearance of being pushed in is stronger.
- [NSButton.GradientType.convexWeak](nsbutton/gradienttype/convexweak.md)
  The top-left corner is dark gray, and the bottom-right corner is light gray, so the button appears to be sticking out.
- [NSButton.GradientType.convexStrong](nsbutton/gradienttype/convexstrong.md)
  As with `NSGradientConvexWeak`, the top-left corner is dark gray, and the bottom-right corner is light gray, but the difference between the grays is greater, so the appearance of sticking out is stronger.
### Initializers
- [init?(rawValue: UInt)](nsbutton/gradienttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum.md)
  The set of bezel styles to style buttons in your app.
- [NSButton.ButtonType](nsbutton/buttontype.md)
  Button types that you can specify using [`setButtonType(_:)`](nsbuttoncell/setbuttontype(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/gradienttype)*