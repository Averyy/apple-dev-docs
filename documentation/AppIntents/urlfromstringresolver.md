# URLFromStringResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts a string into a URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct URLFromStringResolver
```

## Topics

### Resolving the type
- [func resolve(from: String, context: IntentParameterContext<URL>) async throws -> URL?](urlfromstringresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (URLFromStringResolver, URLFromStringResolver) -> Bool](urlfromstringresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](urlfromstringresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](urlfromstringresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [URLFromStringResolver.Input](urlfromstringresolver/input.md)
- [URLFromStringResolver.Output](urlfromstringresolver/output.md)
### Default Implementations
- [Equatable Implementations](urlfromstringresolver/equatable-implementations.md)
- [Resolver Implementations](urlfromstringresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlfromstringresolver)*