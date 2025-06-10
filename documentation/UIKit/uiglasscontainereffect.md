# UIGlassContainerEffect

**Framework**: UIKit  
**Kind**: class

A `UIGlassContainerEffect` renders multiple glass elements into a combined effect.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class UIGlassContainerEffect
```

#### Overview

When using `UIGlassContainerEffect` with a `UIVisualEffectView` you can add individual glass elements to the visual effect view’s contentView by nesting `UIVisualEffectView`‘s configured with `UIGlassEffect`. In that configuration, the glass container will render all glass elements in one combined view, behind the visual effect view’s `contentView`.

## Topics

### Instance Properties
- [var spacing: CGFloat](uiglasscontainereffect/spacing.md)
  The spacing specifies the distance between elements at which they begin to merge.

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

- [class UIGlassEffect](uiglasseffect.md)
  A visual effect that renders a glass material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiglasscontainereffect)*