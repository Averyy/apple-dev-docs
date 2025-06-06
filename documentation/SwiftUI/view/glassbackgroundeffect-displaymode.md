# glassBackgroundEffect(_:displayMode:)

**Framework**: SwiftUI  
**Kind**: method

Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
nonisolated
func glassBackgroundEffect<S>(_ effect: S, displayMode: GlassBackgroundDisplayMode = .always) -> some View where S : GlassBackgroundEffect
```

#### Return Value

A view with a glass background.

#### Discussion

Use this modifier to add a glass material that may include thickness, specularity, glass blur, shadows, and other effects. Because of its physical depth, the background influences z-axis layout. For different effect, the bakcground may influences x-axis and y-axis layout.

To ensure that the effect renders properly when you add it to a collection of views in a [`ZStack`](zstack.md), add the modifier to the stack rather to one of the views in the stack. This includes when you create an implicit stack with view modifiers like [`overlay(alignment:content:)`](view/overlay(alignment:content:).md) or [`background(alignment:content:)`](view/background(alignment:content:).md). In those cases, you might need to create an explicit [`ZStack`](zstack.md) inside the `content` closure to have a place to add the background modifier.

Non closed shapes will be rendered as their convex hull.

## Parameters

- `effect`: A   instance that SwiftUI uses to   draw a background of the modified view.
- `displayMode`: When to display the glass background. The default is   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/glassbackgroundeffect(_:displaymode:))*