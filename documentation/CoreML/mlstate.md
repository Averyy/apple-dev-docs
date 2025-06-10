# MLState

**Framework**: Core ML  
**Kind**: class

Handle to the state buffers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class MLState
```

#### Overview

A stateful model maintains a state from one prediction to another by storing the information in the state buffers. To use such a model, the client must request the model to create state buffers and get `MLState` object, which is the handle to those buffers. Then, at the prediction time, pass the `MLState` object in one of the stateful prediction functions.

```swift
// Load a stateful model
let modelAsset = try MLModelAsset(url: modelURL)
let model = try await MLModel.load(asset: modelAsset, configuration: MLModelConfiguration())

// Request a state
let state = model.newState()

// Run predictions
for _ in 0 ..< 42 {
  _ = try await model.prediction(from: inputFeatures, using: state)
}

// Access the state buffer.
state.withMultiArray(for: "accumulator") { stateMultiArray in
  ...
}
```

The object is a handle to the state buffers. The client shall not read or write the buffers while a prediction is in-flight.

Each stateful prediction that uses the same `MLState` must be serialized. Otherwise, if two such predictions run concurrently, the behavior is undefined.

## Topics

### Instance Methods
- [func withMultiArray<R>((MLMultiArray) -> R) throws -> R](mlstate/withmultiarray(_:).md)
- [func withMultiArray<R>(for: String, (MLMultiArray) throws -> R) rethrows -> R](mlstate/withmultiarray(for:_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MLStateConstraint](mlstateconstraint.md)
  Constraint of a state feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlstate)*