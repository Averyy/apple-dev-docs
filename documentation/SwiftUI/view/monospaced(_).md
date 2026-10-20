# monospaced(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func monospaced(_ isActive: Bool = true) -> some View
```

#### Return Value

A view whose child views’ fonts use fixed-width characters, while leaving other characters proportionally spaced.

#### Discussion

If a child view’s base font doesn’t support fixed-width, the font remains unchanged.

## See Also

### Controlling text style
- [func bold(Bool) -> some View](./bold%28_%29.md)
  Applies a bold font weight to the text in this view.
- [func italic(Bool) -> some View](./italic%28_%29.md)
  Applies italics to the text in this view.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](./underline%28_,pattern,color%29.md)
  Applies an underline to the text in this view.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](./strikethrough%28_,pattern,color%29.md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](./textcase%28_%29.md)
  Sets a transform for the case of the text contained in this view when displayed.
- [var textCase: Text.Case?](../environmentvalues/textcase.md)
  A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [func monospacedDigit() -> some View](./monospaceddigit%28%29.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [protocol AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)
  A protocol for defining how text can be styled in a view.
- [protocol AttributedTextValueConstraint](../attributedtextvalueconstraint.md)
  A protocol for defining a constraint on the value of a certain attribute.
- [enum AttributedTextFormatting](../attributedtextformatting.md)
  A namespace for types related to attributed text formatting definitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/monospaced(_:))*