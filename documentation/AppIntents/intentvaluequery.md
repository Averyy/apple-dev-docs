# IntentValueQuery

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

A query that provides entity values to the system; for example, for visual intelligence search.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol IntentValueQuery : PersistentlyIdentifiable, _SupportsAppDependencies, Sendable
```

## Topics

### Associated Types
- [associatedtype Input : _IntentValue](./intentvaluequery/input.md)
- [associatedtype Result : ResultsCollection = [Self.ResultValue]](./intentvaluequery/result.md)
- [associatedtype ResultValue = Self.Result.Result.ValueType](./intentvaluequery/resultvalue.md)
### Initializers
- [init()](./intentvaluequery/init%28%29.md)
### Instance Methods
- [func values(for: Self.Input) async throws -> Self.Result](./intentvaluequery/values%28for%29.md)
### Type Aliases
- [IntentValueQuery.ExecutionTargets](./intentvaluequery/executiontargets.md)
### Type Properties
- [static var allowedExecutionTargets: IntentExecutionTargets](./intentvaluequery/allowedexecutiontargets.md)
  A set of targets that can run this query.

## Relationships

### Inherits From
- [PersistentlyIdentifiable](./persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Intent queries
- [struct IntentValueContainer](./intentvaluecontainer.md)
  A container that stores a value that supports intent value conversion.
- [struct IntentValueExpression](./intentvalueexpression.md)
  A type that represents a lazily evaluated intent value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluequery)*