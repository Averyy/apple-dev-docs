# SerialModelExecutor

**Framework**: SwiftData  
**Kind**: protocol

An interface for performing serial storage-related tasks using an isolated model context.

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
protocol SerialModelExecutor : ModelExecutor, SerialExecutor
```

## Relationships

### Inherits From
- [Executor](../swift/executor.md)
- [ModelExecutor](modelexecutor.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SerialExecutor](../swift/serialexecutor.md)
### Conforming Types
- [DefaultSerialModelExecutor](defaultserialmodelexecutor.md)

## See Also

- [class DefaultSerialModelExecutor](defaultserialmodelexecutor.md)
  An object that safely performs storage-related tasks using an isolated model context.
- [protocol ModelExecutor](modelexecutor.md)
  An interface for performing storage-related tasks using an isolated model context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/serialmodelexecutor)*