# presentationBackgroundInteraction(_:)

**Framework**: RealityKit  
**Kind**: method

Controls whether people can interact with the view behind a presentation.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst ?+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func presentationBackgroundInteraction(_ interaction: PresentationBackgroundInteraction) -> some View
```

#### Discussion

On many platforms, SwiftUI automatically disables the view behind a sheet that you present, so that people can’t interact with the backing view until they dismiss the sheet. Use this modifier if you want to enable interaction.

The following example enables people to interact with the view behind the sheet when the sheet is at the smallest detent, but not at the other detents:

```None
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents(
                    [.height(120), .medium, .large])
                .presentationBackgroundInteraction(
                    .enabled(upThrough: .height(120)))
        }
    }
}
```

## Parameters

- `interaction`: A specification of how people can interact with the   view behind a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/presentationbackgroundinteraction(_:))*