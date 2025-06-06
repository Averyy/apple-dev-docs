# presentationDetents(_:selection:)

**Framework**: FamilyControls  
**Kind**: method

Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func presentationDetents(_ detents: Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View
```

#### Discussion

By default, sheets support the `PresentationDetent/large` detent.

```swift
struct ContentView: View {
    @State private var showSettings = false
    @State private var settingsDetent = PresentationDetent.medium

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents(
                    [.medium, .large],
                    selection: $settingsDetent
                 )
        }
    }
}
```

## Parameters

- `detents`: A set of supported detents for the sheet.   If you provide more that one detent, people can drag the sheet   to resize it.
- `selection`: A   to the currently selected detent.   Ensure that the value matches one of the detents that you   provide for the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/presentationdetents(_:selection:))*