# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs regression on a shaped array.

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
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> FullyConnectedNetworkRegressorModel<Scalar>.Target
```

#### Return Value

A regression.

## Parameters

- `input`: The regressor input.
- `eventHandler`: An event handler.

## See Also

- [FullyConnectedNetworkRegressorModel.Target](fullyconnectednetworkregressormodel/target.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressormodel/applied(to:eventhandler:))*