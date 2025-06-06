# contentTransition(_:)

**Framework**: SwiftUI  
**Kind**: method

Modifies the view to use a given transition as its method of animating changes to the contents of its views.

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
nonisolated
func contentTransition(_ transition: ContentTransition) -> some View
```

#### Discussion

This modifier allows you to perform a transition that animates a change within a single view. The provided [`ContentTransition`](contenttransition.md) can present an opacity animation for content changes, an interpolated animation of the content’s paths as they change, or perform no animation at all.

> 💡 **Tip**: The `contentTransition(_:)` modifier only has an effect within the context of an [`Animation`](animation.md).

The `contentTransition(_:)` modifier only has an effect within the context of an [`Animation`](animation.md).

In the following example, a [`Button`](button.md) changes the color and font size of a [`Text`](text.md) view. Since both of these properties apply to the paths of the text, the [`interpolate`](contenttransition/interpolate.md) transition can animate a gradual change to these properties through the entire transition. By contrast, the [`opacity`](contenttransition/opacity.md) transition would simply fade between the start and end states.

```swift
private static let font1 = Font.system(size: 20)
private static let font2 = Font.system(size: 45)

@State private var color = Color.red
@State private var currentFont = font1

var body: some View {
    VStack {
        Text("Content transition")
            .foregroundColor(color)
            .font(currentFont)
            .contentTransition(.interpolate)
        Spacer()
        Button("Change") {
            withAnimation(Animation.easeInOut(duration: 5.0)) {
                color = (color == .red) ? .green : .red
                currentFont = (currentFont == font1) ? font2 : font1
            }
        }
    }
}
```

This example uses an ease-in–ease-out animation with a five-second duration to make it easier to see the effect of the interpolation. The figure below shows the `Text` at the beginning of the animation, halfway through, and at the end.

| Time | Display |
| --- | --- |
| Start | ![The text Content transition in a small red font.](https://docs-assets.developer.apple.com/published/eba2db780339b6fbbd97763e652ad3b2/ContentTransition-1%402x.png) |
| Middle | ![The text Content transition in a medium brown font.](https://docs-assets.developer.apple.com/published/746174d6317e87efbfe56c78d5e18a17/ContentTransition-2%402x.png) |
| End | ![The text Content transition in a large green font.](https://docs-assets.developer.apple.com/published/534b62d2cd433733bbf2df631ad7fb5c/ContentTransition-3%402x.png) |

To control whether content transitions use GPU-accelerated rendering, set the value of the [`contentTransitionAddsDrawingGroup`](environmentvalues/contenttransitionaddsdrawinggroup.md) environment variable.

## Parameters

- `transition`: The transition to apply when animating the   content change.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contenttransition(_:))*