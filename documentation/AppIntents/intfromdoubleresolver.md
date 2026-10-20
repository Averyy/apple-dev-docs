# IntFromDoubleResolver

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A resolver that converts a double into an integer using the specified rounding rule and validates the result is within the parameter’s inclusive range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct IntFromDoubleResolver
```

## Topics

### Creating the resolver
- [init(roundingRule: FloatingPointRoundingRule)](./intfromdoubleresolver/init%28roundingrule%29.md)
### Getting the rounding rule
- [var roundingRule: FloatingPointRoundingRule](./intfromdoubleresolver/roundingrule.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RangeCheckingResolver](./rangecheckingresolver.md)
- [Resolver](./resolver.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Integer resolution
- [struct IntFromStringResolver](./intfromstringresolver.md)
  A resolver that converts a string into an integer in the specified base and validates the result is within the parameter’s inclusive range.
- [struct IntResolver](./intresolver.md)
  A resolver that validates an integer is within the parameter’s inclusive range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intfromdoubleresolver)*