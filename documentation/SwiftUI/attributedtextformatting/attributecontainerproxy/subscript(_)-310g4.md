# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Access the value of an attribute that may or may not be in the scope of the associated formatting definition.

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
subscript<K>(key: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { mutating get }
```

**Other overloads**:

```swift
subscript(key: Attribute.Type) -> Attribute.Value? { get set }
```

```swift
subscript<S>(scope: S.Type) -> AttributedTextFormatting.AttributeContainerProxy<Scope, Attribute>.Scoped<S> where S : AttributeScope { get set }
```

## Overview

For details on how attribute value constraining works, refer to [`constrain(_:)`](../../attributedtextvalueconstraint/constrain%28_%29.md).

> **Note**: This subscript provides access to attributes that are not guaranteed to be in scope for the associated text formatting definition. Make sure to document the dependency on `K` as detailed in [`AttributedTextValueConstraint`](../../attributedtextvalueconstraint.md). If `K` is not in `Scope`, this subscript always returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript(_:)-310g4)*