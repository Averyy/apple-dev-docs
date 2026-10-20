# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Reshapes the input.

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
func applied(to input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) throws -> MLShapedArray<Scalar>
```

#### Return Value

A shaped array with the target shape.

## Parameters

- `input`: A shaped array.
- `eventHandler`: An event handler.

## See Also

### Performing the transformation
- [func applied<S>(S, eventHandler: EventHandler?) throws -> [MLShapedArray<Scalar>]](./applied%28_,eventhandler%29.md)
  Reshapes a sequence of inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/reshaper/applied(to:eventhandler:))*