# DefaultSerialModelExecutor

**Framework**: SwiftData  
**Kind**: class

An object that safely performs storage-related tasks using an isolated model context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
class DefaultSerialModelExecutor
```

## Topics

### Creating a model executor
- [init(modelContext: ModelContext)](defaultserialmodelexecutor/init(modelcontext:).md)
### Accessing the context
- [let modelContext: ModelContext](defaultserialmodelexecutor/modelcontext.md)
### Default Implementations
- [Executor Implementations](defaultserialmodelexecutor/executor-implementations.md)
- [SerialExecutor Implementations](defaultserialmodelexecutor/serialexecutor-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Executor](../Swift/Executor.md)
- [ModelExecutor](modelexecutor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SerialExecutor](../Swift/SerialExecutor.md)
- [SerialModelExecutor](serialmodelexecutor.md)

## See Also

- [protocol SerialModelExecutor](serialmodelexecutor.md)
  An interface for performing serial storage-related tasks using an isolated model context.
- [protocol ModelExecutor](modelexecutor.md)
  An interface for performing storage-related tasks using an isolated model context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultserialmodelexecutor)*