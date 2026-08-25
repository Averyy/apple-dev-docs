# presentationPreventsAppTermination(_:)

**Framework**: SwiftUI  
**Kind**: method

Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
nonisolated
func presentationPreventsAppTermination(_ prevents: Bool?) -> some View
```

#### Discussion

SwiftUI uses the buttons in a sheet’s toolbar to determine whether a particular sheet should block termination by default. If there is a singular toolbar item with the [`confirmationAction`](toolbaritemplacement/confirmationaction.md) or the [`cancellationAction`](toolbaritemplacement/cancellationaction.md) placement and no other toolbar items, the sheet will not prevent termination by default.

Use this modifier to specify whether a sheet should prevent app termination. Pass `nil` to explicitly request the automatic behavior/for the inert version of this modifier. Non-nil values will override `nil`, and `true` takes precedence over `false`.

Use this modifier within the `content` argument to `View/sheet`

```swift
struct LaunchScreen: View {
  @State private var presentLogin = false
  var body: some View {
    HomeView()
      .sheet(isPresented: $presentLogin) {
        LoginView()
          // explicitly allow app termination because the
          // default behavior would resolve to `true`.
          .presentationPreventsAppTermination(false)
          .toolbar {
            ToolbarItem(placement: .cancellationAction) {
              Button("Cancel") { presentLogin = false }
            }
            ToolbarItem(placement: .confirmationAction) {
              Button("Login") {
                // Attempt login...
                presentLogin = false
              }
            }
          }
        }
    }
}
```

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
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](view/presentationbreakthrougheffect(_:).md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationPlacement(PresentationPlacement) -> some View](view/presentationplacement(_:).md)
  Sets the placement of a presentation within the presenting view.
- [struct PresentationPlacement](presentationplacement.md)
  The placement of a presentation within the presenting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationpreventsapptermination(_:))*