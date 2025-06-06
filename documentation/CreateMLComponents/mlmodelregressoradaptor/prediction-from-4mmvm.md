# prediction(from:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction from a sequence of inputs.

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
func prediction<S>(from input: S) async throws -> [Self.Output] where S : Sequence, Self.Input == S.Element
```

#### Return Value

An array of regressions.

## Parameters

- `input`: The input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelregressoradaptor/prediction(from:)-4mmvm)*