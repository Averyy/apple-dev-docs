# UIGlassContainerEffect

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A `UIGlassContainerEffect` renders multiple glass elements into a combined effect.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+

## Declaration

```swift
@MainActor
class UIGlassContainerEffect
```

```objc
@interface UIGlassContainerEffect : UIVisualEffect
```

## Overview

When using `UIGlassContainerEffect` with a `UIVisualEffectView` you can add individual glass elements to the visual effect view’s contentView by nesting `UIVisualEffectView`‘s configured with `UIGlassEffect`. In that configuration, the glass container will render all glass elements in one combined view, behind the visual effect view’s `contentView`.

## Topics

### Instance Properties
- [var spacing: CGFloat](./uiglasscontainereffect/spacing.md)
  The spacing specifies the distance between elements at which they begin to merge.

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

### Liquid Glass effects
- [class UIGlassEffect](./uiglasseffect.md)
  A visual effect that renders a glass material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiglasscontainereffect)*