# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Returns the attribute that corresponds to a specified key path.

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
subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## See Also

- [subscript<T>(T.Type) -> T.Value?](attributecontainer/subscript(_:).md)
  Returns the attribute that corresponds to a specified key.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](attributecontainer/subscript(dynamicmember:)-3jcvx.md)
  Returns the attribute container that corresponds to a specified key path.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](attributecontainer/subscript(dynamicmember:)-60ps5.md)
  Returns a modified attribute container as part of building a chain of attributes.
- [static subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](attributecontainer/subscript(dynamicmember:)-swift.type.subscript.md)
  Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [protocol AttributedStringKey](attributedstringkey.md)
  A type that defines an attribute’s name and type.
- [AttributeContainer.Builder](attributecontainer/builder.md)
  A type that iteratively builds attribute containers by setting attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/subscript(dynamicmember:)-657oj)*