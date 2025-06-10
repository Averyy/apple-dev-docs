# SurroundingsEffect

**Framework**: SwiftUI  
**Kind**: struct

Effects that the system can apply to passthrough video.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct SurroundingsEffect
```

#### Overview

Use one of these values with the [`preferredSurroundingsEffect(_:)`](view/preferredsurroundingseffect(_:).md) view modifier to indicate what effect to apply to passthrough video when the modified view is displayed.

## Topics

### Getting the effect
- [static var systemDark: SurroundingsEffect](surroundingseffect/systemdark.md)
  An effect that dims passthrough video.
### Type Properties
- [static var dark: SurroundingsEffect](surroundingseffect/dark.md)
  An effect that dims passthrough video.
- [static var semiDark: SurroundingsEffect](surroundingseffect/semidark.md)
  An effect that dims passthrough video less than [`dark`](surroundingseffect/dark.md).
- [static var ultraDark: SurroundingsEffect](surroundingseffect/ultradark.md)
  An effect that dims passthrough video more than [`dark`](surroundingseffect/dark.md)
### Type Methods
- [static func colorMultiply(Color) -> SurroundingsEffect](surroundingseffect/colormultiply(_:).md)
  An effect that applies a custom tint to the passthrough video by multiplying the passthrough with a [`Color`](color.md).
- [static func dim(intensity: Double) -> SurroundingsEffect](surroundingseffect/dim(intensity:).md)
  An effect that dims the passthrough video a custom amount.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](view/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [struct BreakthroughEffect](breakthrougheffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surroundingseffect)*