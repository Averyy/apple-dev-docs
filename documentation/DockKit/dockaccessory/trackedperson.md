# DockAccessory.TrackedPerson

**Framework**: DockKit  
**Kind**: struct

The state of a tracked person in the active tracking session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct TrackedPerson
```

## Topics

### Operators
- [static func == (DockAccessory.TrackedPerson, DockAccessory.TrackedPerson) -> Bool](dockaccessory/trackedperson/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var identifier: UUID](dockaccessory/trackedperson/identifier.md)
  A unique identifier representing the tracked person. This identifier persists as long as the dock tracks the person. The value is random and doesn’t persist across sessions.
- [var lookingAtCameraConfidence: Double?](dockaccessory/trackedperson/lookingatcameraconfidence.md)
  The confidence of the person looking directly at the camera. The range is from `0.0` to `1.0`, or `nil` if the framework hasn’t calculated the score.
- [var rect: CGRect](dockaccessory/trackedperson/rect.md)
  The bounding box rectangle of the tracked person’s face in the frame.
- [var saliencyRank: Int?](dockaccessory/trackedperson/saliencyrank.md)
  The saliency rank of the person the dock is tracking. A lower rank indicates higher importance of the person. This property is `nil` if the saliency ranking isn’t set or the person isn’t salient.
- [var speakingConfidence: Double?](dockaccessory/trackedperson/speakingconfidence.md)
  The confidence score of the person speaking at the moment of tracking. The range is from `0.0` to `1.0`, or `nil` if the framework hasn’t calculated the score.
### Default Implementations
- [Equatable Implementations](dockaccessory/trackedperson/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/trackedperson)*