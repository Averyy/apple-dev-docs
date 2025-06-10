# presentationCompactAdaptation(horizontal:vertical:)

**Framework**: App Intents  
**Kind**: method

Specifies how to adapt a presentation to horizontally and vertically compact size classes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func presentationCompactAdaptation(horizontal horizontalAdaptation: PresentationAdaptation, vertical verticalAdaptation: PresentationAdaptation) -> some View
```

#### Discussion

Some presentations adapt their appearance depending on the context. For example, a popover presentation over a horizontally-compact view uses a sheet appearance by default. Use this modifier to indicate a custom adaptation preference.

```swift
struct ContentView: View {
    @State private var showInfo = false

    var body: some View {
        Button("View Info") {
            showInfo = true
        }
        .popover(isPresented: $showInfo) {
            InfoView()
                .presentationCompactAdaptation(
                    horizontal: .popover,
                    vertical: .sheet)
        }
    }
}
```

If you want to specify the same adaptation for both dimensions, use the `View/presentationCompactAdaptation(_:)` method instead.

## Parameters

- `horizontalAdaptation`: The adaptation to use in a horizontally   compact size class.
- `verticalAdaptation`: The adaptation to use in a vertically compact   size class. In a size class that is both horizontally and vertically   compact, SwiftUI uses the   value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/presentationcompactadaptation(horizontal:vertical:))*