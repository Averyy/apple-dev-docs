# prediction(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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
func prediction<S, Label>(from input: S) async throws -> [ClassificationDistribution<Label>] where S : Sequence, Label : Hashable, Self.Input == S.Element, Self.Output == ClassificationDistribution<Label>
```

**Other overloads**:

```swift
func prediction<Label>(from input: Self.Input) async throws -> ClassificationDistribution<Label> where Label : Hashable, Self.Output == ClassificationDistribution<Label>
```

## Return Value

An array of classification distributions.

## Parameters

- `input`: The input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/prediction(from:)-107lm)*