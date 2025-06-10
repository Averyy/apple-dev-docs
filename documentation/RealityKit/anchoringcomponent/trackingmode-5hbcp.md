# AnchoringComponent.TrackingMode

**Framework**: RealityKit  
**Kind**: struct

Options for how an entity tracks its target anchor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct TrackingMode
```

## Topics

### Type Properties
- [static let continuous: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-5hbcp/continuous.md)
  Continuously anchors the entity to its target based on the target’s realtime location and hides the entity when the target is no longer in frame.
- [static let once: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-5hbcp/once.md)
  Anchors the entity to the target on the first frame the target is found.
- [static let predicted: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-5hbcp/predicted.md)
  Continuously anchors the entity to its target based on the target’s predicted location and hides the entity when the target is no longer in frame.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/trackingmode-5hbcp)*