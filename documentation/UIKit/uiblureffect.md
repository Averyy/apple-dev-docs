# UIBlurEffect

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that applies a blurring effect to the content layered behind a visual effect view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBlurEffect
```

```objc
@interface UIBlurEffect : UIVisualEffect
```

#### Overview

Views that you add to the [`contentView`](./uivisualeffectview/contentview.md) of a visual effect view aren’t affected by the blur effect.

## Topics

### Creating a blur effect
- [init(style: UIBlurEffect.Style)](./uiblureffect/init%28style%29.md)
  Creates a blur effect with the designated style.
### Constants
- [UIBlurEffect.Style](./uiblureffect/style.md)
  Blur styles available for blur effect objects.

## Relationships

### Inherits From
- [UIVisualEffect](./uivisualeffect.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Visual effects
- [class UIVisualEffect](./uivisualeffect.md)
  An initializer for visual effect views and blur and vibrancy effect objects.
- [class UIVisualEffectView](./uivisualeffectview.md)
  An object that implements some complex visual effects.
- [class UIVibrancyEffect](./uivibrancyeffect.md)
  An object that amplifies and adjusts the color of the content layered behind a visual effect view.
- [class UIColorEffect](./uicoloreffect.md)
  A visual effect that applies a solid color background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiblureffect)*