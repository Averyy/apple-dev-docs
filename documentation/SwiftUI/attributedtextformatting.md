# AttributedTextFormatting

**Framework**: SwiftUI  
**Kind**: enum

A namespace for types related to attributed text formatting definitions.

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
enum AttributedTextFormatting
```

#### Overview

> **Note**: [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md), `View/attributedTextFormattingDefinition(_:)-uc57`

## Topics

### Structures
- [AttributedTextFormatting.AnyDefinition](attributedtextformatting/anydefinition.md)
  A type-erased text formatting definition.
- [AttributedTextFormatting.AttributeContainerProxy](attributedtextformatting/attributecontainerproxy.md)
  A proxy for a partially validated set of attributes.
- [AttributedTextFormatting.DefinitionBuilder](attributedtextformatting/definitionbuilder.md)
  A result builder for attributed text formatting definition.
- [AttributedTextFormatting.EmptyDefinition](attributedtextformatting/emptydefinition.md)
  A text formatting definition that places no constraints on the values of attributes.
- [AttributedTextFormatting.Transferable](attributedtextformatting/transferable.md)
  A transferable representation of an attributed string interpreted in a SwiftUI environment.
- [AttributedTextFormatting.TupleDefinition](attributedtextformatting/tupledefinition.md)
  A text formatting definition that enforces the constraints of a series of text formatting definitions.
- [AttributedTextFormatting.ValueConstraint](attributedtextformatting/valueconstraint.md)
  A text formatting definition that constrains the value of a single attribute to the members of a set.

## See Also

- [func bold(Bool) -> some View](view/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func italic(Bool) -> some View](view/italic(_:).md)
  Applies italics to the text in this view.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](view/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [var textCase: Text.Case?](environmentvalues/textcase.md)
  A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [func monospaced(Bool) -> some View](view/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](view/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [protocol AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)
  A protocol for defining how text can be styled in a view.
- [protocol AttributedTextValueConstraint](attributedtextvalueconstraint.md)
  A protocol for defining a constraint on the value of a certain attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting)*