# ModelActor

**Framework**: SwiftData  
**Kind**: protocol

An interface for providing mutually-exclusive access to the attributes of a conforming model.

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
protocol ModelActor : Actor
```

## Topics

### Accessing the container and context
- [var modelContainer: ModelContainer](modelactor/modelcontainer.md)
  The ModelContainer for the ModelActor The container that manages the app’s schema and model storage configuration
- [var modelContext: ModelContext](modelactor/modelcontext.md)
  The context that serializes any code running on the model actor.
### Accessing the executors
- [var modelExecutor: any ModelExecutor](modelactor/modelexecutor.md)
  The executor that coordinates access to the model actor.
- [var unownedExecutor: UnownedSerialExecutor](modelactor/unownedexecutor.md)
  The optimized, unonwned reference to the model actor’s executor.
### Accessing specific models
- [subscript<T>(PersistentIdentifier, as _: T.Type) -> T?](modelactor/subscript(_:as:).md)
  Returns the model for the specified identifier, downcast to the appropriate class.

## Relationships

### Inherits From
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [macro ModelActor()](modelactor().md)
  Converts a Swift actor into a model actor by generating boilerplate code that fulfills the requirements of the associated protocol.
- [class DefaultSerialModelExecutor](defaultserialmodelexecutor.md)
  An object that safely performs storage-related tasks using an isolated model context.
- [protocol SerialModelExecutor](serialmodelexecutor.md)
  An interface for performing serial storage-related tasks using an isolated model context.
- [protocol ModelExecutor](modelexecutor.md)
  An interface for performing storage-related tasks using an isolated model context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelactor)*