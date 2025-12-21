# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The constraints of the formatting definition.

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
@AttributedTextFormatting
.DefinitionBuilder<Self.Scope> var body: Self.Body { get }
```

#### Discussion

When you implement a custom definition, you must implement a computed `body` property to provide the constraints of your definition. Return a definition that’s composed of built-in definitions that SwiftUI provides, such as [`AttributedTextFormattingDefinition.ValueConstraint`](attributedtextformattingdefinition/valueconstraint.md) and [`AttributedTextValueConstraint`](attributedtextvalueconstraint.md)s, plus other composite [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md)s that you’ve already defined:

```swift
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
```

Note that the order of the constraints in the result builder matters as constraints are applied in order. For details, see `AttributedTextValueConstraint/constrain(_:)-(Attributes)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition/body-1b01t)*