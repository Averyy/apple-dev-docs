# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Predicts human body action periods from an array of poses.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to input: [Pose], eventHandler: EventHandler? = nil) async throws -> [HumanBodyActionPeriodPredictor.Prediction]
```

#### Return Value

An async sequence of predictions.

## Parameters

- `input`: An async sequence of pose windows.
- `eventHandler`: An event handler.

## See Also

- [HumanBodyActionPeriodPredictor.Prediction](humanbodyactionperiodpredictor/prediction.md)
  A human body action period prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactionperiodpredictor/applied(to:eventhandler:))*