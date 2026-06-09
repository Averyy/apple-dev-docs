# searchSelection(_:)

**Framework**: SwiftUI  
**Kind**: method

Binds the selection of the search field associated with the nearest searchable modifier to the given [`TextSelection`](textselection.md) value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func searchSelection(_ selection: Binding<TextSelection?>) -> some View
```

#### Discussion

Use this modifier to read and set selection in your search interface. Selection is represented using `TextSelection` where the indices are relative to the search text you provide on the [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md) modifier. Note that this value will not represent selection outside of the text, such as in any leading tokens.

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

## See Also

- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:isPresented:placement:prompt:)](view/searchable(text:ispresented:placement:prompt:).md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](view/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchToolbarBehavior(SearchToolbarBehavior) -> some View](view/searchtoolbarbehavior(_:).md)
  Configures the behavior for search in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchselection(_:))*