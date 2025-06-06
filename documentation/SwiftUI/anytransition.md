# AnyTransition

**Framework**: SwiftUI  
**Kind**: struct

A type-erased transition.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct AnyTransition
```

#### Overview

- See Also: `Transition`

## Topics

### Getting built-in transitions
- [static let identity: AnyTransition](anytransition/identity.md)
  A transition that returns the input view, unmodified, as the output view.
- [static func move(edge: Edge) -> AnyTransition](anytransition/move(edge:).md)
  Returns a transition that moves the view away, towards the specified edge of the view.
- [static func offset(CGSize) -> AnyTransition](anytransition/offset(_:).md)
- [static func offset(x: CGFloat, y: CGFloat) -> AnyTransition](anytransition/offset(x:y:).md)
- [static let opacity: AnyTransition](anytransition/opacity.md)
  A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static func push(from: Edge) -> AnyTransition](anytransition/push(from:).md)
  Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [static var scale: AnyTransition](anytransition/scale.md)
  Returns a transition that scales the view.
- [static func scale(scale: CGFloat, anchor: UnitPoint) -> AnyTransition](anytransition/scale(scale:anchor:).md)
  Returns a transition that scales the view by the specified amount.
- [static var slide: AnyTransition](anytransition/slide.md)
  A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
### Combining and configuring transitions
- [func animation(Animation?) -> AnyTransition](anytransition/animation(_:).md)
  Attaches an animation to this transition.
- [static func asymmetric(insertion: AnyTransition, removal: AnyTransition) -> AnyTransition](anytransition/asymmetric(insertion:removal:).md)
  Provides a composite transition that uses a different transition for insertion versus removal.
- [func combined(with: AnyTransition) -> AnyTransition](anytransition/combined(with:).md)
  Combines this transition with another, returning a new transition that is the result of both transitions being applied.
### Creating a custom transition
- [init<T>(T)](anytransition/init(_:).md)
  Create an instance that type-erases `transition`.
- [static func modifier<E>(active: E, identity: E) -> AnyTransition](anytransition/modifier(active:identity:).md)
  Returns a transition defined between an active modifier and an identity modifier.

## See Also

- [func transition(_:)](view/transition(_:).md)
  Associates a transition with the view.
- [protocol Transition](transition.md)
  A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [struct TransitionProperties](transitionproperties.md)
  The properties a `Transition` can have.
- [enum TransitionPhase](transitionphase.md)
  An indication of which the current stage of a transition.
- [struct AsymmetricTransition](asymmetrictransition.md)
  A composite `Transition` that uses a different transition for insertion versus removal.
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
- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [protocol NavigationTransition](navigationtransition.md)
  A type that defines the transition to use when navigating to a view.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](view/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](view/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [protocol MatchedTransitionSourceConfiguration](matchedtransitionsourceconfiguration.md)
  A configuration that defines the appearance of a matched transition source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytransition)*