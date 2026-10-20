# prediction(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func prediction<S>(from input: S) async throws -> [Self.Output] where S : Sequence, Self.Input == S.Element
```

#### Return Value

A regression.

## Parameters

- `input`: The input feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/regressor/prediction(from:))*