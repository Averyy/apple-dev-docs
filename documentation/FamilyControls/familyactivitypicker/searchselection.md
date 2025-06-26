# searchSelection(_:)

**Framework**: FamilyControls  
**Kind**: method

Binds the selection of the search field associated with the nearest searchable modifier to the given `TextSelection` value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func searchSelection(_ selection: Binding<TextSelection?>) -> some View
```

#### Discussion

Use this modifier to read and set selection in your search interface. Selection is represented using `TextSelection` where the indices are relative to the search text you provide on the `View/searchable(text:placement:prompt:)` modifier. Note that this value will not represent selection outside of the text, such as in any leading tokens.

SwiftUI will automatically update this value when the user changes selection, such as by typing. Likewise, you can change selection by writing to this value.

The following example creates a search interface that selects all of the text on focus.

```swift
struct ContentView: View {
    @State var text = "Hello, world!"
    @State var selection: TextSelection?
    @FocusState var focused

    var body: some View {
        NavigationSplitView {
            Sidebar()
                .searchable(text: $text)
                .searchFocused($focused)
                .searchSelection($selection)
        } detail: {
            Detail()
        }
        .onChange(of: focused) {
            if focused {
                selection = TextSelection(
                    range: text.startIndex..<text.endIndex)
            }
        }
    }
}
```

## Parameters

- `selection`: The selection value to bind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/searchselection(_:))*