# applied(toWindow:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction on a window of input features.

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
func applied(toWindow input: MLShapedArray<Scalar>, eventHandler: EventHandler? = nil) async throws -> MLShapedArray<Scalar>
```

#### Return Value

A shaped array of predictions with shape `[forecastWindowSize, annotationSize]`.

## Parameters

- `input`: An window of input features with shape  .
- `eventHandler`: An event handler.

## See Also

- [func applied(to:eventHandler:)](lineartimeseriesforecaster/model/applied(to:eventhandler:).md)
  Performs a prediction on a shaped array of features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model/applied(towindow:eventhandler:))*