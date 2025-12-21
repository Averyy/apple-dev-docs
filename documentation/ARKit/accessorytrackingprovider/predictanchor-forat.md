# predictAnchor(for:at:)

**Framework**: ARKit  
**Kind**: method

Predict an accessory anchor to a target timestamp.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final func predictAnchor(for anchor: AccessoryAnchor, at timestamp: TimeInterval) -> AccessoryAnchor?
```

#### Return Value

The predicted anchor, or nil if prediction failed.

#### Discussion

> **Note**: A large time offset from latest anchor timestamp could degrade accuracy. For accuracy sensitive use cases like drawing, use a small offset or `latestAnchors`. Use a prediction timestamp smaller than the latest anchor timestamp for interpolation.

## Parameters

- `anchor`: A tracked anchor from   to generate prediction for.
- `timestamp`: Target time for prediction. For rendering use cases with CompositorServices, use  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/predictanchor(for:at:))*