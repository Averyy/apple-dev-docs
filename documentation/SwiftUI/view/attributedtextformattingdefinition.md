# attributedTextFormattingDefinition(_:)

**Framework**: SwiftUI  
**Kind**: method

Apply a text formatting definition to nested views.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func attributedTextFormattingDefinition<D>(_ definition: D) -> some View where D : AttributedTextFormattingDefinition
```

#### Discussion

Applying a text formatting definition to a [`Text`](text.md) or [`TextEditor`](texteditor.md) created using the [`init(_:)`](text/init(_:)-1a4oh.md) or [`init(text:selection:)`](texteditor/init(text:selection:).md) initializer, respectively, makes sure that any content observable to the user adheres to the constraints of the formatting definition.

You can compose your own definition from an attribute scope and a series of [`AttributedTextValueConstraint`](attributedtextvalueconstraint.md)s:

```swift
// MyTextFormattingDefinition.swift

struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
        MyAttributedTextValueConstraint()
    }
}

// MyEditorView.swift

TextEditor(text: $text)
    .attributedTextFormattingDefinition(MyTextFormattingDefinition())
```

> **Note**: A [`Binding`](binding.md) to the text of a view with an [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md) may still contain values that do not adhere to text formatting definition. E.g., a [`TextEditor`](texteditor.md) may choose to not apply constraints in the text formatting definition to parts of a bound attributed string that are not visible on screen.

To manually enforce constraints, e.g. before serializing text contents, use the [`constrain(_:)`](attributedtextformattingdefinition/constrain(_:)-1ur9c.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/attributedtextformattingdefinition(_:))*