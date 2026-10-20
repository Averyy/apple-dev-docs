# presentationPreventsAppTermination(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
nonisolated
func presentationPreventsAppTermination(_ prevents: Bool?) -> some View
```

#### Discussion

SwiftUI uses the buttons in a sheet’s toolbar to determine whether a particular sheet should block termination by default. If there is a singular toolbar item with the [`confirmationAction`](../toolbaritemplacement/confirmationaction.md) or the [`cancellationAction`](../toolbaritemplacement/cancellationaction.md) placement and no other toolbar items, the sheet will not prevent termination by default.

Use this modifier to specify whether a sheet should prevent app termination. Pass `nil` to explicitly request the automatic behavior/for the inert version of this modifier. Non-nil values will override `nil`, and `true` takes precedence over `false`.

Use this modifier within the `content` argument to [`sheet(isPresented:onDismiss:content:)`](./sheet%28ispresented,ondismiss,content%29.md)

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

### Sheet and popover configuration
- [func interactiveDismissDisabled(Bool) -> some View](./interactivedismissdisabled%28_%29.md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func presentationDetents(Set<PresentationDetent>) -> some View](./presentationdetents%28_%29.md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](./presentationdetents%28_,selection%29.md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](./presentationdragindicator%28_%29.md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationBackground<S>(S) -> some View](./presentationbackground%28_%29.md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](./presentationbackground%28alignment,content%29.md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./presentationbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](./presentationcompactadaptation%28horizontal,vertical%29.md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](./presentationcompactadaptation%28_%29.md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](./presentationcontentinteraction%28_%29.md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](./presentationcornerradius%28_%29.md)
  Requests that the presentation have a specific corner radius.
- [func presentationSizing(some PresentationSizing) -> some View](./presentationsizing%28_%29.md)
  Sets the sizing of the containing presentation.
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](./presentationbreakthrougheffect%28_%29.md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationPlacement(PresentationPlacement) -> some View](./presentationplacement%28_%29.md)
  Sets the placement of a presentation within the presenting view.
- [struct PresentationPlacement](../presentationplacement.md)
  The placement of a presentation within the presenting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationpreventsapptermination(_:))*