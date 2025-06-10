# AttributeDynamicLookup

**Framework**: Foundation  
**Kind**: enum

A type to support dynamic member lookup of attributes and containers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@dynamicMemberLookup
@frozen enum AttributeDynamicLookup
```

#### Overview

This type allows attribute owners to add extensions that enable dynamic member lookup access to attributes. Supporting types — including [`AttributedString`](attributedstring.md), [`AttributedSubstring`](attributedsubstring.md), and [`AttributeContainer`](attributecontainer.md) — gain dynamic lookup support by extending this type.

You can enable dynamic member lookup for your own [`AttributedStringKey`](attributedstringkey.md) attributes by defining them as implementations, collecting them into an [`AttributeScope`](attributescope.md) and extending [`AttributeDynamicLookup`](attributedynamiclookup.md), like in the following example:

```swift
public extension AttributeDynamicLookup {
    subscript<T: AttributedStringKey>(dynamicMember keyPath: KeyPath<AttributeScopes.MyFrameworkAttributes, T>) -> T {
        return self[T.self]
    }
}
```

## Topics

### Accessing Key Values
- [subscript<T>(T.Type) -> T](attributedynamiclookup/subscript(_:).md)
  Returns an attributed string key that corresponds to a specified type.
### Accessing Framework Attribute Scopes
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3nor6.md)
  Returns the attributed string key for a specified Foundation key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes.NumberFormatAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3neai.md)
  Returns the attributed string key for a specified Foundation number format key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.SwiftUIAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3q4ap.md)
  Returns the attributed string key for a specified SwiftUI key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.UIKitAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-4yyyo.md)
  Returns the attributed string key for a specified UIKit key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.AppKitAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3v1cn.md)
  Returns the attributed string key for a specified AppKit key path.
### Subscripts
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-30vmv.md)
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.SpeechAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3ft4y.md)
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.AccessibilityAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-7vcf2.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [enum AttributeScopes](attributescopes.md)
  Collections of attributes that system frameworks define.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedynamiclookup)*