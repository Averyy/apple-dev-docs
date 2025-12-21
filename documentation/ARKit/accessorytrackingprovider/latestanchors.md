# latestAnchors

**Framework**: ARKit  
**Kind**: property

The latest accessory anchors updated with the most recent inertial data.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final var latestAnchors: [AccessoryAnchor] { get }
```

#### Discussion

These anchors provide higher frequency, lower latency and slightly lower accuracy than `anchorUpdates`. Use them directly or in combination with `predictAnchor(for:at:)`.

The array may be empty if the provider is not running or no accessory is tracked at the moment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/latestanchors)*