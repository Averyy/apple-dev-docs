# UIBlurEffect

**Framework**: UIKit  
**Kind**: class

An object that applies a blurring effect to the content layered behind a visual effect view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBlurEffect
```

#### Overview

Views that you add to the [`contentView`](uivisualeffectview/contentview.md) of a visual effect view aren’t affected by the blur effect.

## Topics

### Creating a blur effect
- [init(style: UIBlurEffect.Style)](uiblureffect/init(style:).md)
  Creates a blur effect with the designated style.
### Constants
- [UIBlurEffect.Style](uiblureffect/style.md)
  Blur styles available for blur effect objects.

## Relationships

### Inherits From
- [UIVisualEffect](uivisualeffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIVisualEffect](uivisualeffect.md)
  An initializer for visual effect views and blur and vibrancy effect objects.
- [class UIVisualEffectView](uivisualeffectview.md)
  An object that implements some complex visual effects.
- [class UIVibrancyEffect](uivibrancyeffect.md)
  An object that amplifies and adjusts the color of the content layered behind a visual effect view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiblureffect)*