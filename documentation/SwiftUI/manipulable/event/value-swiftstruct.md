# Manipulable.Event.Value

**Framework**: SwiftUI  
**Kind**: struct

Describes the value associated with a manipulation gesture event.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Value
```

## Topics

### Instance Properties
- [let frame: Rect3D](manipulable/event/value-swift.struct/frame.md)
  The 3D bounding box of the manipulated view.
- [let inputDevices: [Manipulable.InputDevice]](manipulable/event/value-swift.struct/inputdevices.md)
  The input devices that a person is using to manipulate a view.
- [let interactionPoint: Point3D](manipulable/event/value-swift.struct/interactionpoint.md)
  The point at which a person interacted with a view to begin manipulating it.
- [let timestamp: TimeInterval](manipulable/event/value-swift.struct/timestamp.md)
  The time the event was processed.
- [let transform: AffineTransform3D?](manipulable/event/value-swift.struct/transform.md)
  The 3D affine transform of the manipulated view, or `nil` if the view doesn’t have a well-defined 3D affine transfrorm.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulable/event/value-swift.struct)*