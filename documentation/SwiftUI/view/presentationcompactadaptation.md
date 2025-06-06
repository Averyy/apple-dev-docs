# presentationCompactAdaptation(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies how to adapt a presentation to compact size classes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func presentationCompactAdaptation(_ adaptation: PresentationAdaptation) -> some View
```

#### Discussion

Some presentations adapt their appearance depending on the context. For example, a sheet presentation over a vertically-compact view uses a full-screen-cover appearance by default. Use this modifier to indicate a custom adaptation preference. For example, the following code uses a presentation adaptation value of [`none`](presentationadaptation/none.md) to request that the system not adapt the sheet in compact size classes:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents([.medium, .large])
                .presentationCompactAdaptation(.none)
        }
    }
}
```

If you want to specify different adaptations for each dimension, use the [`presentationCompactAdaptation(horizontal:vertical:)`](view/presentationcompactadaptation(horizontal:vertical:).md) method instead.

## Parameters

- `adaptation`: The adaptation to use in either a horizontally   or vertically compact size class.

## See Also

- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](view/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [struct PresentationAdaptation](presentationadaptation.md)
  Strategies for adapting a presentation to a different size class.
- [func presentationSizing(some PresentationSizing) -> some View](view/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [protocol PresentationSizing](presentationsizing.md)
  A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [struct PresentationSizingRoot](presentationsizingroot.md)
  A proxy to a view provided to the presentation with a defined presentation size.
- [struct PresentationSizingContext](presentationsizingcontext.md)
  Contextual information about a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationcompactadaptation(_:))*