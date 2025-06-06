# prediction(from:)

**Framework**: Create ML Components  
**Kind**: method

Performs a prediction from a single input.

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
func prediction(from input: Self.Input) async throws -> Self.Output
```

#### Return Value

A regression.

## Parameters

- `input`: The input feature.

## See Also

- [func prediction<S>(from: S) async throws -> [Self.Output]](regressor/prediction(from:)-7iqkm.md)
  Performs a prediction from a sequence of inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/regressor/prediction(from:)-7gc68)*