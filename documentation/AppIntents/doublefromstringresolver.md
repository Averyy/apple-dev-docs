# DoubleFromStringResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts a string into a double and validates the result is within the parameter’s inclusive range.

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
struct DoubleFromStringResolver
```

## Topics

### Resolving the type
- [func resolve(from: String, context: IntentParameterContext<Double>) async throws -> Double?](doublefromstringresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (DoubleFromStringResolver, DoubleFromStringResolver) -> Bool](doublefromstringresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](doublefromstringresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](doublefromstringresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [DoubleFromStringResolver.Input](doublefromstringresolver/input.md)
- [DoubleFromStringResolver.Output](doublefromstringresolver/output.md)
### Default Implementations
- [Equatable Implementations](doublefromstringresolver/equatable-implementations.md)
- [RangeCheckingResolver Implementations](doublefromstringresolver/rangecheckingresolver-implementations.md)
- [Resolver Implementations](doublefromstringresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RangeCheckingResolver](rangecheckingresolver.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DoubleFromIntResolver](doublefromintresolver.md)
- [struct DoubleResolver](doubleresolver.md)
  A resolver that validates a double is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/doublefromstringresolver)*