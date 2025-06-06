# StringFromIntResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts one or more integers into one or more strings.

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
struct StringFromIntResolver<Input, Output> where Input : _IntentValue, Output : _IntentValue, Output.ValueType == String
```

## Topics

### Resolving the type
- [func resolve(from: Input, context: IntentParameterContext<Output>) async throws -> Output?](stringfromintresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (StringFromIntResolver<Input, Output>, StringFromIntResolver<Input, Output>) -> Bool](stringfromintresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](stringfromintresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](stringfromintresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](stringfromintresolver/equatable-implementations.md)
- [Resolver Implementations](stringfromintresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AttributedStringFromStringResolver](attributedstringfromstringresolver.md)
  A resolver that converts a string into an attributed string.
- [struct StringFromDoubleResolver](stringfromdoubleresolver.md)
  A resolver that converts a double into a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringfromintresolver)*