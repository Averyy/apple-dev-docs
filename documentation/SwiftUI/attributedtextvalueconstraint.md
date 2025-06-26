# AttributedTextValueConstraint

**Framework**: SwiftUI  
**Kind**: protocol

A protocol for defining a constraint on the value of a certain attribute.

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
protocol AttributedTextValueConstraint : Hashable, Sendable, AttributedTextFormattingDefinition
```

#### Overview

Used as an [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md), this constrains the [`AttributeKey`](attributedtextvalueconstraint/attributekey.md)’s value using the `constrain(_:)-(Attributes)` function.

A simple constraint only accesses a single attribute. It can be made generic over the attribute scope so it can be reused in different [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md)s.

```swift
struct NoBlackOrWhiteForeground<Scope: AttributeScope>: AttributedTextValueConstraint {
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if container.foregroundColor == .white || container.foregroundColor == .black {
            container.foregroundColor = .primary
        }
    }
}
```

When the constraint needs to access other attribute values, it is recommended to define it on a specific attribute scope that is used for a single [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md).

```swift
extension MyTextFormattingDefinition {
    struct Scope: AttributeScope {
        /* ... */
        let foregroundColor: AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute
        let backgroundColor: AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute
    }
}

struct NoEqualForegroundAndBackground: AttributedTextValueConstraint {
    typealias Scope = MyTextFormattingDefinition.Scope
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if let color = container.foregroundColor,
           container.backgroundColor == color
        {
            container.backgroundColor = nil
        }
    }
}
```

Constraints that access multiple attributes and are generic over the scope should document their dependencies so that they can be considered for the ordering of constraints in the [`body`](attributedtextformattingdefinition/body-1b01t.md).

```swift
/// Makes the background color for all Genmoji blue.
///
/// - Note: This constraint depends on a valid adaptiveImageGlyph value.
struct BlueGenmojiBackgroundConstraint<Scope: AttributeScope>: AttributedTextValueConstraint {
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes
        .BackgroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if container[
            AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute.self
        ] != nil {
            container.backgroundColor = .blue
        }
    }
}
```

## Topics

### Associated Types
- [associatedtype AttributeKey : AttributedStringKey](attributedtextvalueconstraint/attributekey.md)
  The attribute constrained by this constraint.
### Instance Methods
- [func constrain(inout Self.Attributes)](attributedtextvalueconstraint/constrain(_:).md)
  Enforce constraints on the attribute.
### Type Aliases
- [AttributedTextValueConstraint.Attributes](attributedtextvalueconstraint/attributes.md)
  A proxy type for a container of partially constrained attributes.

## Relationships

### Inherits From
- [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
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
- [protocol AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)
  A protocol for defining how text can be styled in a certain context, e.g. a `TextEditor`.
- [enum AttributedTextFormatting](attributedtextformatting.md)
  A namespace for types related to attributed text formatting definitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextvalueconstraint)*