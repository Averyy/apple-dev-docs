# DoubleFromIntResolver

**Framework**: App Intents  
**Kind**: struct

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
struct DoubleFromIntResolver
```

## Topics

### Resolving the type
- [func resolve(from: Int, context: IntentParameterContext<Double>) async throws -> Double?](doublefromintresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Operators
- [static func == (DoubleFromIntResolver, DoubleFromIntResolver) -> Bool](doublefromintresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](doublefromintresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](doublefromintresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [DoubleFromIntResolver.Input](doublefromintresolver/input.md)
- [DoubleFromIntResolver.Output](doublefromintresolver/output.md)
### Default Implementations
- [Equatable Implementations](doublefromintresolver/equatable-implementations.md)
- [RangeCheckingResolver Implementations](doublefromintresolver/rangecheckingresolver-implementations.md)
- [Resolver Implementations](doublefromintresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RangeCheckingResolver](rangecheckingresolver.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DoubleFromStringResolver](doublefromstringresolver.md)
  A resolver that converts a string into a double and validates the result is within the parameter’s inclusive range.
- [struct DoubleResolver](doubleresolver.md)
  A resolver that validates a double is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/doublefromintresolver)*