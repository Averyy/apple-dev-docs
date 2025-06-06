# presentationCompactAdaptation(_:)

**Framework**: Assignables  
**Kind**: method

Specifies how to adapt a presentation to compact size classes.

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
func presentationCompactAdaptation(_ adaptation: PresentationAdaptation) -> some View
```

#### Discussion

Some presentations adapt their appearance depending on the context. For example, a sheet presentation over a vertically-compact view uses a full-screen-cover appearance by default. Use this modifier to indicate a custom adaptation preference. For example, the following code uses a presentation adaptation value of `PresentationAdaptation/none` to request that the system not adapt the sheet in compact size classes:

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
                .presentationCompactAdaptation(.none)
        }
    }
}
```

If you want to specify different adaptations for each dimension, use the `View/presentationCompactAdaptation(horizontal:vertical:)` method instead.

## Parameters

- `adaptation`: The adaptation to use in either a horizontally   or vertically compact size class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/presentationcompactadaptation(_:))*