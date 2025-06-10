# BoolFromStringResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts a string into a Boolean, optionally using a localized display name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct BoolFromStringResolver
```

## Topics

### Resolving the type
- [func resolve(from: String, context: IntentParameterContext<Bool>) async throws -> Bool?](boolfromstringresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (BoolFromStringResolver, BoolFromStringResolver) -> Bool](boolfromstringresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](boolfromstringresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](boolfromstringresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [BoolFromStringResolver.Input](boolfromstringresolver/input.md)
- [BoolFromStringResolver.Output](boolfromstringresolver/output.md)
### Default Implementations
- [Equatable Implementations](boolfromstringresolver/equatable-implementations.md)
- [Resolver Implementations](boolfromstringresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/boolfromstringresolver)*