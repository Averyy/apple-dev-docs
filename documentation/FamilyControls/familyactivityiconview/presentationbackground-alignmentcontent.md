# presentationBackground(alignment:content:)

**Framework**: FamilyControls  
**Kind**: method

Sets the presentation background of the enclosing sheet to a custom view.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func presentationBackground<V>(alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Discussion

The following example uses a yellow view as the sheet background:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationBackground {
                    Color.yellow
                }
        }
    }
}
```

The `presentationBackground(alignment:content:)` modifier differs from the `View/background(alignment:content:)` modifier in several key ways. A presentation background:

- Automatically fills the entire presentation.
- Allows views behind the presentation to show through translucent areas of the `content`.

## Parameters

- `alignment`: The alignment that the modifier uses to position the   implicit   that groups the background views. The default is   .
- `content`: The view to use as the background of the presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/presentationbackground(alignment:content:))*