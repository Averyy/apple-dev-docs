# AttributedTextFormatting.TupleDefinition

**Framework**: SwiftUI  
**Kind**: struct

A text formatting definition that enforces the constraints of a series of text formatting definitions.

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