# predictAnchor(for:at:)

**Framework**: ARKit  
**Kind**: method

Get an `AccessoryAnchor` for a given time and accessory.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func predictAnchor(for anchor: AccessoryAnchor, at timestamp: TimeInterval) -> AccessoryAnchor?
```

#### Return Value

The predicted anchor, or nil if prediction failed.

## Parameters

- `anchor`: A tracked anchor to generate prediction for. Applications which do not wish to receive routine anchor updates can request them as-needed with  .
- `timestamp`: Target time for prediction. When rendering with CompositorServices this should be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/predictanchor(for:at:))*