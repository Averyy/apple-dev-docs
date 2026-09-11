# init(value:expectations:)

**Framework**: Evaluations  
**Kind**: init

Creates a model sample output with an optional expected value and expectations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
init(value: Value? = nil, expectations: Expectation? = nil)
```

#### Discussion

```swift
let output = ModelSampleOutput<String, TrajectoryExpectation>(value: "Paris", expectations: nil)
```

## Parameters

- `value`: The expected output value for comparison.
- `expectations`: The expected behavior, such as a tool-call trajectory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleoutput/init(value:expectations:))*