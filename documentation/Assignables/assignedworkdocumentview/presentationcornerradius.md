# presentationCornerRadius(_:)

**Framework**: Assignables  
**Kind**: method

Requests that the presentation have a specific corner radius.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func presentationCornerRadius(_ cornerRadius: CGFloat?) -> some View
```

#### Discussion

Use this modifier to change the corner radius of a presentation.

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
                .presentationCornerRadius(21)
        }
    }
}
```

## Parameters

- `cornerRadius`: The corner radius, or   to use the system   default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/presentationcornerradius(_:))*