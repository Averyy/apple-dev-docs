# textCase(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets a transform for the case of the text contained in this view when displayed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func textCase(_ textCase: Text.Case?) -> some View
```

#### Return Value

A view that transforms the case of the text.

#### Discussion

The default value is `nil`, displaying the text without any case changes.

## Parameters

- `textCase`: One of the   enumerations; the   default is  .

## See Also

- [func bold(Bool) -> some View](view/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func italic(Bool) -> some View](view/italic(_:).md)
  Applies italics to the text in this view.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](view/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [var textCase: Text.Case?](environmentvalues/textcase.md)
  A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [func monospaced(Bool) -> some View](view/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](view/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [protocol AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)
  A protocol for defining how text can be styled in a certain context, e.g. a `TextEditor`.
- [protocol AttributedTextValueConstraint](attributedtextvalueconstraint.md)
  A protocol for defining a constraint on the value of a certain attribute.
- [enum AttributedTextFormatting](attributedtextformatting.md)
  A namespace for types related to attributed text formatting definitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textcase(_:))*