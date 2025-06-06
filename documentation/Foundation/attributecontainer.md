# AttributeContainer

**Framework**: Foundation  
**Kind**: struct

A container for attribute keys and values.

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
struct AttributeContainer
```

#### Overview

[`AttributeContainer`](attributecontainer.md) provides a way to store attributes and their values outside of an attributed string. You use this type to initialize an instance of [`AttributedString`](attributedstring.md) with preset attributes, and to set, merge, or replace attributes in existing attributed strings.

## Topics

### Creating an Attribute Container
- [init()](attributecontainer/init.md)
  Creates an empty attribute container.
- [init<S>([NSAttributedString.Key : Any], including: S.Type) throws](attributecontainer/init(_:including:)-2mw0o.md)
  Creates an attribute container from a dictionary and an attribute scope.
- [init<S>([NSAttributedString.Key : Any], including: KeyPath<AttributeScopes, S.Type>) throws](attributecontainer/init(_:including:)-28n0g.md)
  Creates an attribute container from a dictionary and an attribute scope that a key path identifies.
- [init([NSAttributedString.Key : Any])](attributecontainer/init(_:).md)
  Creates an attribute container from a dictionary, using default attribute scopes.
### Accessing Attributes
- [subscript<T>(T.Type) -> T.Value?](attributecontainer/subscript(_:).md)
  Returns the attribute that corresponds to a specified key.
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
### Modifying Attributes
- [func merge(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributecontainer/merge(_:mergepolicy:).md)
  Merges the container’s attributes with those in another attribute container.
- [func merging(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy) -> AttributeContainer](attributecontainer/merging(_:mergepolicy:).md)
  Returns an attribute container by merging the container’s attributes with those in another attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
### Interoperating with Objective-C Attributes
- [protocol ObjectiveCConvertibleAttributedStringKey](objectivecconvertibleattributedstringkey.md)
  A protocol that defines Objective-C interoperability with an attribute key’s value type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DecodableWithConfiguration](decodablewithconfiguration.md)
- [EncodableWithConfiguration](encodablewithconfiguration.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init()](attributedstring/init.md)
  Creates an empty attributed string.
- [init(AttributedSubstring)](attributedstring/init(_:)-8tnoq.md)
  Creates an attributed string from an attributed substring.
- [init(String, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-2a45h.md)
  Creates an attributed string from a string and an attribute container.
- [init(Substring, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-8jqhp.md)
  Creates an attributed string from a substring and an attribute container.
- [init<S>(S, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-8l0iq.md)
  Creates an attributed string from a character sequence and an attribute container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer)*