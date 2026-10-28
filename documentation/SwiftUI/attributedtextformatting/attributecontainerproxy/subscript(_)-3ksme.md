# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Create a scoped version of this attribute container to disambiguate access to attributes with overloaded names.

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
subscript<S>(scope: S.Type) -> AttributedTextFormatting.AttributeContainerProxy<Scope, Attribute>.Scoped<S> where S : AttributeScope { get set }
```

**Other overloads**:

```swift
subscript(key: Attribute.Type) -> Attribute.Value? { get set }
```

```swift
subscript<K>(key: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { mutating get }
```

## Overview

Use this subscript to e.g. make sure you are accessing the SwiftUI `font`, not the font attribute defined by UIKit or AppKit:

```swift
if container.[AttributesScopes.SwiftUIAttributes.self].font == nil { /* ... *? }
```

> **Note**: This subscript provides access to attributes that are not guaranteed to be in scope for the associated text formatting definition. Make sure to document such attribute dependencies as detailed in [`AttributedTextValueConstraint`](../../attributedtextvalueconstraint.md). If an attribute is not in `Scope`, its subscript always returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript(_:)-3ksme)*