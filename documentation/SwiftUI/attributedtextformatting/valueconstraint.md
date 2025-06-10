# AttributedTextFormatting.ValueConstraint

**Framework**: SwiftUI  
**Kind**: struct

A text formatting definition that constrains the value of a single attribute to the members of a set.

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
struct ValueConstraint<Scope, AttributeKey> where Scope : AttributeScope, AttributeKey : AttributedStringKey, AttributeKey.Value : Sendable
```

#### Overview

```swift
struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        // Allow no underline or the `.single` underline style. If
        // a text has any other underline style, it is corrected
        // to the default value `.single`
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
    }
}
```

## Topics

### Initializers
- [init(for:values:default:)](attributedtextformatting/valueconstraint/init(for:values:default:).md)
  Create a definition that constrains an attribute’s value to a defined set of allowed values.

## Relationships

### Conforms To
- [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)
- [AttributedTextValueConstraint](attributedtextvalueconstraint.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/valueconstraint)*