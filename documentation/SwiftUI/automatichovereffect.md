# AutomaticHoverEffect

**Framework**: SwiftUI  
**Kind**: struct

The default hover effect based on the surrounding context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct AutomaticHoverEffect
```

#### Overview

The automatic effect will resolve to any [`defaultHoverEffect(_:)`](view/defaulthovereffect(_:).md) applied to the current View hierarchy, or a system-defined effect if no default effect has been defined.

You can also use [`automatic`](customhovereffect/automatic.md) to construct this hover effect.

## Topics

### Initializers
- [init()](automatichovereffect/init.md)
  Creates an automatic hover effect.

## Relationships

### Conforms To
- [CustomHoverEffect](customhovereffect.md)

## See Also

- [struct EmptyHoverEffect](emptyhovereffect.md)
  A base hover effect used to build additional effects.
- [struct HighlightHoverEffect](highlighthovereffect.md)
  A hover effect that highlights views using a light source to indicate position.
- [struct LiftHoverEffect](lifthovereffect.md)
  A hover effect that slides the pointer under the view and disappears as the view scales up and gains a shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/automatichovereffect)*