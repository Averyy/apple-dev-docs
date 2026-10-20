# AttributedTextFormatting.AttributeContainerProxy.Scoped

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A scoped proxy for a partially validated set of attributes.

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
struct Scoped<Subscope> where Subscope : AttributeScope
```

Available when `Scope` conforms to `AttributeScope`, `Attribute` conforms to `AttributedStringKey`, and `Attribute.Value` conforms to `Sendable`.

#### Overview

Exposes `Attribute` as read-write and all other attributes in the scope as read-only. The type automatically queries the underlying [`AttributedTextFormattingDefinition`](../../attributedtextformattingdefinition.md) to constrain values that are accessed.

> **Note**: This is equivalent to an [`AttributedTextFormatting.AttributeContainerProxy`](../attributecontainerproxy.md), except it only provides dynamic member lookup for attributes in a certain `Subscope`.

## Topics

### Subscripts
- [subscript(dynamicMember:)](./scoped/subscript%28dynamicmember%29.md)
  Access the value of the attribute to constrain.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/scoped)*