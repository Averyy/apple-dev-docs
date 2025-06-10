# ContentTransition

**Framework**: SwiftUI  
**Kind**: struct

A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ContentTransition
```

#### Overview

Set the behavior of content transitions within a view with the [`contentTransition(_:)`](view/contenttransition(_:).md) modifier, passing in one of the defined transitions, such as [`opacity`](contenttransition/opacity.md) or [`interpolate`](contenttransition/interpolate.md) as the parameter.

> 💡 **Tip**: Content transitions only take effect within transactions that apply an [`Animation`](animation.md) to the views inside the [`contentTransition(_:)`](view/contenttransition(_:).md) modifier.

Content transitions only take effect within the context of an [`Animation`](animation.md) block.

## Topics

### Getting content transitions
- [static let identity: ContentTransition](contenttransition/identity.md)
  The identity content transition, which indicates that content changes shouldn’t animate.
- [static let interpolate: ContentTransition](contenttransition/interpolate.md)
  A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [static func numericText(countsDown: Bool) -> ContentTransition](contenttransition/numerictext(countsdown:).md)
  Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [static func numericText(value: Double) -> ContentTransition](contenttransition/numerictext(value:).md)
  Creates a content transition intended to be used with `Text` views displaying numbers.
- [static let opacity: ContentTransition](contenttransition/opacity.md)
  A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static var symbolEffect: ContentTransition](contenttransition/symboleffect.md)
  A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [static func symbolEffect<T>(T, options: SymbolEffectOptions) -> ContentTransition](contenttransition/symboleffect(_:options:).md)
  Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct AnyTransition](anytransition.md)
  A type-erased transition.
- [func contentTransition(ContentTransition) -> some View](view/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [var contentTransition: ContentTransition](environmentvalues/contenttransition.md)
  The current method of animating the contents of views.
- [var contentTransitionAddsDrawingGroup: Bool](environmentvalues/contenttransitionaddsdrawinggroup.md)
  A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenttransition)*