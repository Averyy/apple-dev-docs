# NSButton.GradientType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Specify the gradients used by the [`gradientType`](../nsbuttoncell/gradienttype.md) property.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

## Declaration

```swift
enum GradientType
```

```c
enum NSGradientType : NSUInteger;
```

## Topics

### Constants
- [NSButton.GradientType.none](./gradienttype/none.md)
  There is no gradient, so the button looks flat.
- [NSButton.GradientType.concaveWeak](./gradienttype/concaveweak.md)
  The top-left corner is light gray, and the bottom-right corner is dark gray, so the button appears to be pushed in.
- [NSButton.GradientType.concaveStrong](./gradienttype/concavestrong.md)
  As with `NSGradientConcaveWeak`, the top-left corner is light gray, and the bottom-right corner is dark gray, but the difference between the grays is greater, so the appearance of being pushed in is stronger.
- [NSButton.GradientType.convexWeak](./gradienttype/convexweak.md)
  The top-left corner is dark gray, and the bottom-right corner is light gray, so the button appears to be sticking out.
- [NSButton.GradientType.convexStrong](./gradienttype/convexstrong.md)
  As with `NSGradientConvexWeak`, the top-left corner is dark gray, and the bottom-right corner is light gray, but the difference between the grays is greater, so the appearance of sticking out is stronger.
### Initializers
- [init?(rawValue: UInt)](./gradienttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/gradienttype)*