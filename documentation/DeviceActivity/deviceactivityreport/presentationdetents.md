# presentationDetents(_:)

**Framework**: DeviceActivity  
**Kind**: method

Sets the available detents for the enclosing sheet.

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
func presentationDetents(_ detents: Set<PresentationDetent>) -> some View
```

#### Discussion

By default, sheets support the `PresentationDetent/large` detent.

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
        }
    }
}
```

## Parameters

- `detents`: A set of supported detents for the sheet.   If you provide more that one detent, people can drag the sheet   to resize it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/presentationdetents(_:))*