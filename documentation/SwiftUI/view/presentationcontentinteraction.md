# presentationContentInteraction(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the behavior of swipe gestures on a presentation.

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
func presentationContentInteraction(_ behavior: PresentationContentInteraction) -> some View
```

#### Discussion

By default, when a person swipes up on a scroll view in a resizable presentation, the presentation grows to the next detent. A scroll view embedded in the presentation only scrolls after the presentation reaches its largest size. Use this modifier to control which action takes precedence.

For example, you can request that swipe gestures scroll content first, resizing the sheet only after hitting the end of the scroll view, by passing the [`scrolls`](presentationcontentinteraction/scrolls.md) value to this modifier:

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
                .presentationContentInteraction(.scrolls)
        }
    }
}
```

People can always resize your presentation using the drag indicator.

## Parameters

- `behavior`: The requested behavior.

## See Also

- [func presentationDetents(Set<PresentationDetent>) -> some View](view/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](view/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](view/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [struct PresentationDetent](presentationdetent.md)
  A type that represents a height where a sheet naturally rests.
- [protocol CustomPresentationDetent](custompresentationdetent.md)
  The definition of a custom detent with a calculated height.
- [struct PresentationContentInteraction](presentationcontentinteraction.md)
  A behavior that you can use to influence how a presentation responds to swipe gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationcontentinteraction(_:))*