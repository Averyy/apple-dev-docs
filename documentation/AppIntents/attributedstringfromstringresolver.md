# AttributedStringFromStringResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts a string into an attributed string.

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
struct AttributedStringFromStringResolver
```

## Topics

### Resolving the type
- [func resolve(from: String, context: IntentParameterContext<AttributedString>) async throws -> AttributedString?](attributedstringfromstringresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (AttributedStringFromStringResolver, AttributedStringFromStringResolver) -> Bool](attributedstringfromstringresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](attributedstringfromstringresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](attributedstringfromstringresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [AttributedStringFromStringResolver.Input](attributedstringfromstringresolver/input.md)
- [AttributedStringFromStringResolver.Output](attributedstringfromstringresolver/output.md)
### Default Implementations
- [Equatable Implementations](attributedstringfromstringresolver/equatable-implementations.md)
- [Resolver Implementations](attributedstringfromstringresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct StringFromDoubleResolver](stringfromdoubleresolver.md)
  A resolver that converts a double into a string.
- [struct StringFromIntResolver](stringfromintresolver.md)
  A resolver that converts one or more integers into one or more strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/attributedstringfromstringresolver)*