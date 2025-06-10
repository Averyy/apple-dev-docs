# AttributedTextFormatting.AttributeContainerProxy.Scoped

**Framework**: SwiftUI  
**Kind**: struct

A scoped proxy for a partially validated set of attributes.

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
@dynamicMemberLookup
struct Scoped<Subscope> where Subscope : AttributeScope
```

#### Overview

Exposes `Attribute` as read-write and all other attributes in the scope as read-only. The type automatically queries the underlying [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md) to constrain values that are accessed.

> **Note**: This is equivalent to an [`AttributedTextFormatting.AttributeContainerProxy`](attributedtextformatting/attributecontainerproxy.md), except it only provides dynamic member lookup for attributes in a certain `Subscope`.

## Topics

### Subscripts
- [subscript(dynamicMember:)](attributedtextformatting/attributecontainerproxy/scoped/subscript(dynamicmember:).md)
  Access the value of the attribute to constrain.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/scoped)*