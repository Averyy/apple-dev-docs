# attributedTextFormattingDefinition(_:)

**Framework**: MusicKit  
**Kind**: method

Apply a text formatting definition to all nested editor views.

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
@MainActor
@preconcurrency func attributedTextFormattingDefinition<D>(_ definition: D) -> some View where D : AttributedTextFormattingDefinition
```

#### Discussion

Applying a text formatting definition to a view makes sure that any content observable to the user adheres to the constraints of the formatting definition.

You can compose your own definition from an attribute scope and a series of `AttributedTextValueConstraint`s:

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

> **Note**: A `Binding` to the text of a view with an `AttributedTextFormattingDefinition` may still contain values that do not adhere to text formatting definition. E.g., a `TextEditor` may choose to not apply constraints in the text formatting definition to parts of a bound attributed string that are not visible on screen.

To manually enforce constraints, e.g. before serializing text contents, use the `AttributedTextValueConstraint/constrain(_:)-6cp64` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/attributedtextformattingdefinition(_:)-6yb2y)*