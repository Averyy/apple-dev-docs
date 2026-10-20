# RangeCheckingResolver

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for validating that a value is within a parameter’s defined inclusive range.

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
protocol RangeCheckingResolver : Resolver
```

## Topics

### Checking the range of a parameter
- [func checkParameterRangeContains<Value>(value: Value, context: IntentParameterContext<Self.Output>) throws](./rangecheckingresolver/checkparameterrangecontains%28value,context%29.md)

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Resolver](./resolver.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [DoubleFromIntResolver](./doublefromintresolver.md)
- [DoubleFromStringResolver](./doublefromstringresolver.md)
- [DoubleResolver](./doubleresolver.md)
- [IntFromDoubleResolver](./intfromdoubleresolver.md)
- [IntFromStringResolver](./intfromstringresolver.md)
- [IntResolver](./intresolver.md)

## See Also

### Range validation
- [protocol RangeComparableProperty](./rangecomparableproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/rangecheckingresolver)*