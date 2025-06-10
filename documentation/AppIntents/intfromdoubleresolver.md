# IntFromDoubleResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts a double into an integer using the specified rounding rule and validates the result is within the parameter’s inclusive range.

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
struct IntFromDoubleResolver
```

## Topics

### Creating the resolver
- [init(roundingRule: FloatingPointRoundingRule)](intfromdoubleresolver/init(roundingrule:).md)
### Resolving the type
- [func resolve(from: Double, context: IntentParameterContext<Int>) async throws -> Int?](intfromdoubleresolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
### Getting the rounding rule
- [var roundingRule: FloatingPointRoundingRule](intfromdoubleresolver/roundingrule.md)
### Operators
- [static func == (IntFromDoubleResolver, IntFromDoubleResolver) -> Bool](intfromdoubleresolver/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intfromdoubleresolver/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intfromdoubleresolver/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [IntFromDoubleResolver.Input](intfromdoubleresolver/input.md)
- [IntFromDoubleResolver.Output](intfromdoubleresolver/output.md)
### Default Implementations
- [Equatable Implementations](intfromdoubleresolver/equatable-implementations.md)
- [RangeCheckingResolver Implementations](intfromdoubleresolver/rangecheckingresolver-implementations.md)
- [Resolver Implementations](intfromdoubleresolver/resolver-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RangeCheckingResolver](rangecheckingresolver.md)
- [Resolver](resolver.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct IntFromStringResolver](intfromstringresolver.md)
  A resolver that converts a string into an integer in the specified base and validates the result is within the parameter’s inclusive range.
- [struct IntResolver](intresolver.md)
  A resolver that validates an integer is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intfromdoubleresolver)*