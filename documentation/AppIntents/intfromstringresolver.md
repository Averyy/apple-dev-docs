# IntFromStringResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts a string into an integer in the specified base and validates the result is within the parameter’s inclusive range.

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
struct IntFromStringResolver
```

## Topics

### Creating the resolver
- [init(radix: Int)](intfromstringresolver/init(radix:).md)
### Resolving the type
- [func resolve(from: String, context: IntentParameterContext<Int>) async throws -> Int?](intfromstringresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Getting the radix setting
- [var radix: Int](intfromstringresolver/radix.md)
### Operators
- [static func == (IntFromStringResolver, IntFromStringResolver) -> Bool](intfromstringresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intfromstringresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intfromstringresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [IntFromStringResolver.Input](intfromstringresolver/input.md)
- [IntFromStringResolver.Output](intfromstringresolver/output.md)
### Default Implementations
- [Equatable Implementations](intfromstringresolver/equatable-implementations.md)
- [RangeCheckingResolver Implementations](intfromstringresolver/rangecheckingresolver-implementations.md)
- [Resolver Implementations](intfromstringresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RangeCheckingResolver](rangecheckingresolver.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IntFromDoubleResolver](intfromdoubleresolver.md)
  A resolver that converts a double into an integer using the specified rounding rule and validates the result is within the parameter’s inclusive range.
- [struct IntResolver](intresolver.md)
  A resolver that validates an integer is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intfromstringresolver)*