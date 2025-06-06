# glassBackgroundEffect(_:in:displayMode:)

**Framework**: SwiftUI  
**Kind**: method

Fills the view’s background with a custom glass background effect and a shape that you specify.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
nonisolated
func glassBackgroundEffect<T, S>(_ effect: S, in shape: T, displayMode: GlassBackgroundDisplayMode = .always) -> some View where T : InsettableShape, S : GlassBackgroundEffect
```

#### Return Value

A view with a glass background.

## Parameters

- `effect`: A   instance that SwiftUI uses to   the fill the background shape that you specify.
- `shape`: An   instance that SwiftUI draws behind   the view.
- `displayMode`: When to display the glass background. The default is   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(_:in:displaymode:))*