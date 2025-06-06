# IntResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that validates an integer is within the parameter’s inclusive range.

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
struct IntResolver
```

## Topics

### Resolving the type
- [func resolve(from: Int, context: IntentParameterContext<Int>) async throws -> Int?](intresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (IntResolver, IntResolver) -> Bool](intresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [IntResolver.Input](intresolver/input.md)
- [IntResolver.Output](intresolver/output.md)
### Default Implementations
- [Equatable Implementations](intresolver/equatable-implementations.md)
- [RangeCheckingResolver Implementations](intresolver/rangecheckingresolver-implementations.md)
- [Resolver Implementations](intresolver/resolver-implementations.md)

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
- [struct IntFromStringResolver](intfromstringresolver.md)
  A resolver that converts a string into an integer in the specified base and validates the result is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intresolver)*