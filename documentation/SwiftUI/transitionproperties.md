# TransitionProperties

**Framework**: SwiftUI  
**Kind**: struct

The properties a `Transition` can have.

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
struct TransitionProperties
```

#### Overview

A transition can have properties that specify high level information about it. This can determine how a transition interacts with other features like Accessibility settings.

- See Also: `Transition`

## Topics

### Creating the transition properties
- [init(hasMotion: Bool)](transitionproperties/init(hasmotion:).md)
- [var hasMotion: Bool](transitionproperties/hasmotion.md)
  Whether the transition includes motion.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func transition(_:)](view/transition(_:).md)
  Associates a transition with the view.
- [protocol Transition](transition.md)
  A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [enum TransitionPhase](transitionphase.md)
  An indication of which the current stage of a transition.
- [struct AsymmetricTransition](asymmetrictransition.md)
  A composite `Transition` that uses a different transition for insertion versus removal.
- [struct AnyTransition](anytransition.md)
  A type-erased transition.
- [func contentTransition(ContentTransition) -> some View](view/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [var contentTransition: ContentTransition](environmentvalues/contenttransition.md)
  The current method of animating the contents of views.
- [var contentTransitionAddsDrawingGroup: Bool](environmentvalues/contenttransitionaddsdrawinggroup.md)
  A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [struct ContentTransition](contenttransition.md)
  A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [struct PlaceholderContentView](placeholdercontentview.md)
  A placeholder used to construct an inline modifier, transition, or other helper type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transitionproperties)*