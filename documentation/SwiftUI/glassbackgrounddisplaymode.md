# GlassBackgroundDisplayMode

**Framework**: SwiftUI  
**Kind**: enum

The display mode of a glass background.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum GlassBackgroundDisplayMode
```

#### Overview

Use a value of this type to indicate when to display a glass background that you add to a view using a view modifier like [`glassBackgroundEffect(displayMode:)`](view/glassbackgroundeffect(displaymode:).md).

## Topics

### Getting the mode
- [GlassBackgroundDisplayMode.always](glassbackgrounddisplaymode/always.md)
  Always display the glass material.
- [GlassBackgroundDisplayMode.implicit](glassbackgrounddisplaymode/implicit.md)
  Display the glass material only when the view isn’t already contained in glass.
- [GlassBackgroundDisplayMode.never](glassbackgrounddisplaymode/never.md)
  Never display the glass material.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbackgrounddisplaymode)*