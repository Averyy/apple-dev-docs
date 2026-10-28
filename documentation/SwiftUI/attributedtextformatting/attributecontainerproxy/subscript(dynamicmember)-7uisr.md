# subscript(dynamicMember:)

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
subscript<S>(dynamicMember keyPath: KeyPath<Scope, S>) -> AttributedTextFormatting.AttributeContainerProxy<Scope, Attribute>.Scoped<S> where S : AttributeScope { get set }
```

**Other overloads**:

```swift
subscript(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, Attribute>) -> Attribute.Value? { get set }
```

```swift
subscript(dynamicMember keyPath: KeyPath<Scope, Attribute>) -> Attribute.Value? { get set }
```

```swift
subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { mutating get }
```

```swift
subscript<K>(dynamicMember keyPath: KeyPath<Scope, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { mutating get }
```

```swift
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> AttributedTextFormatting.AttributeContainerProxy<Scope, Attribute>.Scoped<S> where S : AttributeScope { get set }
```

## Overview

Use this subscript to e.g. make sure you are accessing the SwiftUI `font`, not the font attribute defined by UIKit or AppKit:

```swift
if container.swiftUI.font == nil { /* ... *? }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript(dynamicmember:)-7uisr)*