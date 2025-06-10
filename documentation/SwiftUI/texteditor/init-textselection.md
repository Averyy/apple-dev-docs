# init(text:selection:)

**Framework**: SwiftUI  
**Kind**: init

Creates a styled text editor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
init(text: Binding<AttributedString>, selection: Binding<AttributedTextSelection>? = nil)
```

#### Discussion

Use a [`TextEditor`](texteditor.md) instance to create a view in which users can enter and edit long-form styled text.

In this example the text editor is setup to edit styled text:

```swift
struct StyledTextEditingView: View {
    @State private var fullText =
        AttributedString("This is some editable text...")

    var body: some View {
        TextEditor(text: $fullText)
    }
}
```

If the AttributedString does not have a font and/or foreground color specified for a given range of text, the rich text editor will use the font and/or foreground color inherited from the environment for that range of text.

## Parameters

- `text`: A   to the variable containing the   styled text to edit.
- `selection`: An optional   to the variable   containing the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditor/init(text:selection:))*