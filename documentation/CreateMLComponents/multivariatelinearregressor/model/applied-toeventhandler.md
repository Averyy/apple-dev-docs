# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction on a shaped array.

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
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> MLShapedArray<Scalar>
```

#### Return Value

A shaped array of predictions. The shape of the predictions matches the shape of the input except for the last dimension, which is `outputSize`.

## Parameters

- `input`: A shaped array of features. The last dimension must be  .
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/model/applied(to:eventhandler:))*