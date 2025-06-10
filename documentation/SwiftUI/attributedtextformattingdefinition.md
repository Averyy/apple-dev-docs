# AttributedTextFormattingDefinition

**Framework**: SwiftUI  
**Kind**: protocol

A protocol for defining how text can be styled in a certain context, e.g. a `TextEditor`.

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
protocol AttributedTextFormattingDefinition<Scope>
```

## Topics

### Associated Types
- [associatedtype Body : AttributedTextFormattingDefinition](attributedtextformattingdefinition/body-swift.associatedtype.md)
  The type of view representing the body of this formatting definition.
- [associatedtype Scope : AttributeScope](attributedtextformattingdefinition/scope.md)
  The text formatting definition only allows usage of attributes in this attribute scope.
### Instance Properties
- [var body: Self.Body](attributedtextformattingdefinition/body-1b01t.md)
  The constraints of the formatting definition.
### Instance Methods
- [func constrain(_:)](attributedtextformattingdefinition/constrain(_:).md)
  Applies all value constraints to a given attribute container.
### Type Aliases
- [AttributedTextFormattingDefinition.ValueConstraint](attributedtextformattingdefinition/valueconstraint.md)
  A text formatting definition that permits a single attribute to be used, optionally constrained to a set of values.

## Relationships

### Inherited By
- [AttributedTextValueConstraint](attributedtextvalueconstraint.md)
### Conforming Types
- [AttributedTextFormatting.AnyDefinition](attributedtextformatting/anydefinition.md)
- [AttributedTextFormatting.EmptyDefinition](attributedtextformatting/emptydefinition.md)
- [AttributedTextFormatting.TupleDefinition](attributedtextformatting/tupledefinition.md)
- [AttributedTextFormatting.ValueConstraint](attributedtextformatting/valueconstraint.md)

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
- [protocol AttributedTextValueConstraint](attributedtextvalueconstraint.md)
  A protocol for defining a constraint on the value of a certain attribute.
- [enum AttributedTextFormatting](attributedtextformatting.md)
  A namespace for types related to attributed text formatting definitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition)*