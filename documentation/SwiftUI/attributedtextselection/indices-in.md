# indices(in:)

**Framework**: SwiftUI  
**Kind**: method

The current text selection indices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func indices(in text: AttributedString) -> AttributedTextSelection.Indices
```

#### Return Value

The current selection if valid for the given `text` or a valid fallback index otherwise.

#### Discussion

Always make sure to keep selection and text synchronized. Use `AttributedString/transform(updating:body:)` or `AttributedString/replaceSelection(_:with:)` to do so automatically. Reset your selection manually to a newly initialized one after making programmatic changes to the text where they selection should not just move with the characters.

struct ContentView: View { @State private var text = AttributedString() @State private var selection = AttributedTextSelection()

```swift
var body: some View {
    TextEditor(text: $text, selection: $selection)

    Button("Insert Date") {
        text.replaceSelection(
            &selection,
            withCharacters: Date.now.formatted())
    }

    Button("Reset") {
        text = "Hello, World!"
        selection = .init(range: text.startIndex..<text.endIndex)
    }
}
```

}


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/indices(in:))*