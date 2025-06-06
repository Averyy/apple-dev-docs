# predicted

**Framework**: RealityKit  
**Kind**: property

Continuously anchors the entity to its target based on the target’s predicted location and hides the entity when the target is no longer in frame.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static let predicted: AnchoringComponent.TrackingMode
```

#### Discussion

`predicted` means the `Entity` will be updated whenever the corresponding anchor is updated but its transformation will be `ARKit` prediction.

If the target does not support prediction, `predicted` behaves the same as `continuous`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/trackingmode-swift.struct/predicted)*