# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

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

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire attributed string or substring. To find portions of an attributed string with consistent attributes, use the [`runs`](../attributedstring/runs-swift.property.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## Default Implementations

### AttributedStringProtocol Implementations
- [subscript(RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring](./subscript%28_%29-67hgv.md)
  Returns a discontiguous substring of this attributed string using a set of ranges to indicate the discontiguous substring bounds.

## See Also

### Accessing Whole-String Attributes
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](./subscript%28dynamicmember%29-2wake.md)
  Returns an attribute value that a key path indicates.
- [enum AttributeDynamicLookup](../attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](./subscript%28dynamicmember%29-55pcu.md)
  Returns a scoped attribute container that a key path indicates.
- [struct ScopedAttributeContainer](../scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(_:)-4thnp)*