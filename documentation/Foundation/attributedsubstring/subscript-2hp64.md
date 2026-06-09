# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns an attribute value that corresponds to an attributed string key.

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
@preconcurrency
subscript<K>(_: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

#### Discussion

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire attributed string or substring. To find portions of the string with consistent attributes, use the [`runs`](attributedsubstring/runs.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributedsubstring/subscript(dynamicmember:)-3o8o1.md)
  Returns an attribute value that a key path indicates.
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](attributedsubstring/subscript(dynamicmember:)-548k0.md)
  Returns a scoped attribute container that a key path indicates.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring/subscript(_:)-2hp64)*