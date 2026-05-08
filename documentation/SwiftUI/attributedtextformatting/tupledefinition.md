# AttributedTextFormatting.TupleDefinition

**Framework**: SwiftUI  
**Kind**: struct

A text formatting definition that enforces the constraints of a series of text formatting definitions.

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
struct TupleDefinition<Scope, each Definition> where Scope : AttributeScope, repeat each Definition : AttributedTextFormattingDefinition
```

#### Overview

> **Note**: All sub-definitions are required to have the same `Scope`.

## Topics

### Initializers
- [init(definition: repeat each Definition)](attributedtextformatting/tupledefinition/init(definition:).md)

## Relationships

### Conforms To
- [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/tupledefinition)*