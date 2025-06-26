# init(text:selection:)

**Framework**: SwiftUI  
**Kind**: init

Creates a styled text editor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(text: Binding<AttributedString>, selection: Binding<AttributedTextSelection>? = nil)
```

#### Discussion

Use a [`TextEditor`](texteditor.md) instance to create a view in which users can enter and edit long-form styled text.

In this example the text editor is setup to edit styled text:

```swift
struct StyledTextEditingView: View {
    @State private var text =
        AttributedString("This is some editable text...")

    var body: some View {
        TextEditor(text: $text)
    }
}
```

If the AttributedString does not have a font and/or foreground color specified for a given range of text, the rich text editor will use the font and/or foreground color inherited from the environment for that range of text.

Use [`AttributedTextSelection`](attributedtextselection.md) for implementing custom controls, e.g. for applying formatting such as boldness:

```swift
struct StyledTextEditingView: View {
    @State private var text: AttributedString = ""
    @State private var selection = AttributedTextSelection()

    @Environment(\.fontResolutionContext) private var fontResolutionContext

    var body: some View {
        TextEditor(text: $text, selection: $selection)
            .toolbar {
                // A toggle controlling whether the current selection in the
                // editor has bold font.
                Toggle(
                    "Toggle Boldness",
                    systemImage: "bold",
                    isOn: Binding(get: {
                        // Get the font for the current selection.
                        let font = selection.typingAttributes(in: text).font
                        // Resolve the font in the current environment.
                        let resolved = (font ?? .default).resolve(in: fontResolutionContext)
                        // Return whether the resolved font is bold.
                        return resolved.isBold
                    }, set: { isBold in
                        // Update each run in the current selection, including
                        // the typing attributes, to reflect the new `isBold`
                        // value.
                        text.transformAttributes(in: &selection) {
                            // Override the boldness of the font. If no font is
                            // present, use `Font.default` for the effective
                            // environment font as the basis.
                            $0.font = ($0.font ?? .default).bold(isBold)
                        }
                    })
                )
            }
    }
}
```

> **Note**: When binding the `selection`, always make sure it is updated after you mutate the `text`. Otherwise, the editor resets the selection to the end of the `text`. For more details, see [`indices(in:)`](attributedtextselection/indices(in:).md).

> **Note**: [`AttributedTextSelection`](attributedtextselection.md), `View/attributedTextFormattingDefinition(_:)-uc57`, [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md), [`AttributedTextValueConstraint`](attributedtextvalueconstraint.md), [`AttributedTextFormatting`](attributedtextformatting.md)

## Parameters

- `text`: A   to the variable containing the   styled text to edit.
- `selection`: An optional   to the variable   containing the selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditor/init(text:selection:))*