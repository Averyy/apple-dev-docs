# PhaseAnimator

**Framework**: SwiftUI  
**Kind**: struct

A container that animates its content by automatically cycling through a collection of phases that you provide, each defining a discrete step within an animation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct PhaseAnimator<Phase, Content> where Phase : Equatable, Content : View
```

#### Overview

Use one of the phase animator view modifiers like [`phaseAnimator(_:content:animation:)`](view/phaseanimator(_:content:animation:).md) to create a phased animation in your app.

## Topics

### Creating a phase animator
- [init(some Sequence<Phase>, content: (Phase) -> Content, animation: (Phase) -> Animation?)](phaseanimator/init(_:content:animation:).md)
  Cycles through a sequence of phases continuously, animating updates to a view on each phase change.
- [init(some Sequence<Phase>, trigger: some Equatable, content: (Phase) -> Content, animation: (Phase) -> Animation?)](phaseanimator/init(_:trigger:content:animation:).md)
  Cycles through a sequence of phases in response to changes in a specified value, animating updates to a view on each phase change.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Controlling the timing and movements of your animations](controlling-the-timing-and-movements-of-your-animations.md)
  Build sophisticated animations that you control using phase and keyframe animators.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](view/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](view/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/phaseanimator)*