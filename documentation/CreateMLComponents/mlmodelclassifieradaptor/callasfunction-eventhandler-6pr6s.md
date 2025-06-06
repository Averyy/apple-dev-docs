# callAsFunction(_:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on a sequence of inputs.

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
func callAsFunction<S>(_ input: S, eventHandler: EventHandler? = nil) async throws -> [Self.Output] where S : Sequence, Self.Input == S.Element
```

#### Return Value

The outputs produced by applying the transformer to the inputs.

## Parameters

- `input`: The transformer inputs.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelclassifieradaptor/callasfunction(_:eventhandler:)-6pr6s)*