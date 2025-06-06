# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns the attribute that corresponds to a specified key.

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
subscript<T>(_: T.Type) -> T.Value? where T : AttributedStringKey, T.Value : Sendable { get set }
```

## See Also

- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributecontainer/subscript(dynamicmember:)-657oj.md)
  Returns the attribute that corresponds to a specified key path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/subscript(_:))*