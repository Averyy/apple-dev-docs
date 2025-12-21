# AttributedTextFormatting.AttributeContainerProxy

**Framework**: SwiftUI  
**Kind**: struct

A proxy for a partially validated set of attributes.

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
@dynamicMemberLookup
struct AttributeContainerProxy<Scope, Attribute> where Scope : AttributeScope, Attribute : AttributedStringKey, Attribute.Value : Sendable
```

#### Overview

Exposes `Attribute` as read-write and all other attributes as read-only. The type automatically queries the underlying [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md) to constrain values that are accessed.

## Topics

### Structures
- [AttributedTextFormatting.AttributeContainerProxy.Scoped](attributedtextformatting/attributecontainerproxy/scoped.md)
  A scoped proxy for a partially validated set of attributes.
### Subscripts
- [subscript(_:)](attributedtextformatting/attributecontainerproxy/subscript(_:).md)
  Access the value of the attribute to constrain.
- [subscript(dynamicMember:)](attributedtextformatting/attributecontainerproxy/subscript(dynamicmember:).md)
  Access the value of the attribute to constrain.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy)*