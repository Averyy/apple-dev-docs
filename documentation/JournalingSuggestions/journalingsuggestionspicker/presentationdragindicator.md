# presentationDragIndicator(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets the visibility of the drag indicator on top of a sheet.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func presentationDragIndicator(_ visibility: Visibility) -> some View
```

#### Discussion

You can show a drag indicator when it isn’t apparent that a sheet can resize or when the sheet can’t dismiss interactively.

```None
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents([.medium, .large])
                .presentationDragIndicator(.visible)
        }
    }
}
```

## Parameters

- `visibility`: The preferred visibility of the drag indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/presentationdragindicator(_:))*