# applied(_:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Reshapes a sequence of inputs.

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
func applied<S>(_ input: S, eventHandler: EventHandler? = nil) throws -> [MLShapedArray<Scalar>] where S : Sequence, S.Element == MLShapedArray<Scalar>
```

#### Return Value

An array of shaped arrays.

## Parameters

- `input`: A sequence of input shaped arrays.
- `eventHandler`: An event handler.

## See Also

- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) throws -> MLShapedArray<Scalar>](reshaper/applied(to:eventhandler:).md)
  Reshapes the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/reshaper/applied(_:eventhandler:))*