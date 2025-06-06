# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Updates a fully connected network classifier model with a new sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func update<InputSequence>(_ transformer: inout FullyConnectedNetworkClassifierModel<Scalar, Label>, with input: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, InputSequence.Element == AnnotatedFeature<MLShapedArray<Scalar>, Label>
```

## Parameters

- `transformer`: A fully connected network classifier model to update.
- `input`: A sequence of examples.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/update(_:with:eventhandler:))*