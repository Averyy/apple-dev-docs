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

## See Also

- [func bold(Bool) -> some View](view/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func fontDesign(Font.Design?) -> some View](view/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](view/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](view/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func italic(Bool) -> some View](view/italic(_:).md)
  Applies italics to the text in this view.
- [func monospaced(Bool) -> some View](view/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](view/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](view/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](view/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func textRenderer<T>(T) -> some View](view/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/attributedtextformattingdefinition(_:))*