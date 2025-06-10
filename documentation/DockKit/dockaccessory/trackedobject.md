# DockAccessory.TrackedObject

**Framework**: DockKit  
**Kind**: struct

The state of a tracked object in the active tracking session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct TrackedObject
```

## Topics

### Operators
- [static func == (DockAccessory.TrackedObject, DockAccessory.TrackedObject) -> Bool](dockaccessory/trackedobject/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var identifier: UUID](dockaccessory/trackedobject/identifier.md)
  A unique identifier for the tracked object. This identifier persists as long as the dock tracks the object. The value is random and doesn’t persist across sessions.
- [var rect: CGRect](dockaccessory/trackedobject/rect.md)
  The bounding box rectangle of the tracked object in the frame.
- [var saliencyRank: Int?](dockaccessory/trackedobject/saliencyrank.md)
  The saliency rank of the object the dock is tracking. A lower rank indicates higher importance of the object. This property is `nil` if the saliency ranking isn’t set or the object isn’t salient.
### Default Implementations
- [Equatable Implementations](dockaccessory/trackedobject/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/trackedobject)*