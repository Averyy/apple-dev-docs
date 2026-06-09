# presentationBreakthroughEffect(_:)

**Framework**: SwiftUI  
**Kind**: method

Changes the way the enclosing presentation breaks through content occluding it.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func presentationBreakthroughEffect(_ effect: BreakthroughEffect) -> some View
```

#### Discussion

Use this modifier to disable or customize a breakthrough effect for the enclosing presentation.

Breakthrough is an effect allowing elements to be visible to the user even when other app content (3D models, UI elements) is occluding it. The way the element appears depends on the chosen [`BreakthroughEffect`](breakthrougheffect.md).

Most system presentations appear with a breakthrough effect by default. For these cases, you can customize the type of effect by applying the [`presentationBreakthroughEffect(_:)`](view/presentationbreakthrougheffect(_:).md) modifier to the content of the presentation, like in the following example:

```swift
Button("Show Details") {
    isShowingDetails = true
}
.popover(isPresented: $isShowingDetails) {
    DetailsView()
        .presentationBreakthroughEffect(.prominent)
}
```

Only popovers allow breakthrough to be disabled altogether. Passing a `.none` value for a sheet has no effect.

## Parameters

- `effect`: The type of effect to apply when a presentation element is occluded by other content.

## See Also

- [func interactiveDismissDisabled(Bool) -> some View](view/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func presentationDetents(Set<PresentationDetent>) -> some View](view/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](view/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](view/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationBackground<S>(S) -> some View](view/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](view/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](view/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](view/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](view/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](view/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](view/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationSizing(some PresentationSizing) -> some View](view/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [func presentationPreventsAppTermination(Bool?) -> some View](view/presentationpreventsapptermination(_:).md)
  Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationbreakthrougheffect(_:))*