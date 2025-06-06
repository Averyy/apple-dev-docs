# DoubleResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that validates a double is within the parameter’s inclusive range.

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
struct DoubleResolver
```

## Topics

### Resolving the type
- [func resolve(from: Double, context: IntentParameterContext<Double>) async throws -> Double?](doubleresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (DoubleResolver, DoubleResolver) -> Bool](doubleresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](doubleresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](doubleresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [DoubleResolver.Input](doubleresolver/input.md)
- [DoubleResolver.Output](doubleresolver/output.md)
### Default Implementations
- [Equatable Implementations](doubleresolver/equatable-implementations.md)
- [RangeCheckingResolver Implementations](doubleresolver/rangecheckingresolver-implementations.md)
- [Resolver Implementations](doubleresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RangeCheckingResolver](rangecheckingresolver.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct DoubleFromIntResolver](doublefromintresolver.md)
- [struct DoubleFromStringResolver](doublefromstringresolver.md)
  A resolver that converts a string into a double and validates the result is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/doubleresolver)*