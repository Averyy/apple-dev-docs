# ScopedAttributeContainer

**Framework**: Foundation  
**Kind**: struct

An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.

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
struct ScopedAttributeContainer<S> where S : AttributeScope
```

#### Overview

Use a [`ScopedAttributeContainer`](scopedattributecontainer.md) when you need to disambiguate between attributes that exist in several attribute scopes that your app uses.

## Topics

### Accessing Attribute Keys
- [subscript<T>(dynamicMember _: KeyPath<S, T>) -> T.Value?](scopedattributecontainer/subscript(dynamicmember:).md)
  Returns the value of the attribute that the specified key path indicates.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum AttributeScopes](attributescopes.md)
  Collections of attributes that system frameworks define.
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scopedattributecontainer)*