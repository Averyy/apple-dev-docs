# underline(_:pattern:color:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies an underline to the text in this view.

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
func underline(_ isActive: Bool = true, pattern: Text.LineStyle.Pattern = .solid, color: Color? = nil) -> some View
```

#### Return Value

A view where text has a line running along its baseline.

## Parameters

- `isActive`: A Boolean value that indicates whether underline is added. The default value is `true`.
- `pattern`: The pattern of the line. The default value is `solid`.
- `color`: The color of the underline. If `color` is `nil`, the underline uses the default foreground color.

## See Also

### Controlling text style
- [func bold(Bool) -> some View](./bold%28_%29.md)
  Applies a bold font weight to the text in this view.
- [func italic(Bool) -> some View](./italic%28_%29.md)
  Applies italics to the text in this view.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](./strikethrough%28_,pattern,color%29.md)
  Applies a strikethrough to the text in this view.
- [func textCase(Text.Case?) -> some View](./textcase%28_%29.md)
  Sets a transform for the case of the text contained in this view when displayed.
- [var textCase: Text.Case?](../environmentvalues/textcase.md)
  A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [func monospaced(Bool) -> some View](./monospaced%28_%29.md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](./monospaceddigit%28%29.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [protocol AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)
  A protocol for defining how text can be styled in a view.
- [protocol AttributedTextValueConstraint](../attributedtextvalueconstraint.md)
  A protocol for defining a constraint on the value of a certain attribute.
- [enum AttributedTextFormatting](../attributedtextformatting.md)
  A namespace for types related to attributed text formatting definitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/underline(_:pattern:color:))*