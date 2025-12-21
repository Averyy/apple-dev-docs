# DockAccessory.FramingMode

**Framework**: DockKit  
**Kind**: enum

The mode to control framing of the subject when tracking.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum FramingMode
```

#### Overview

The default is [`DockAccessory.FramingMode.automatic`](dockaccessory/framingmode-swift.enum/automatic.md), which works well for most situations. [`DockAccessory.FramingMode.center`](dockaccessory/framingmode-swift.enum/center.md) keeps the subject close to the middle of frame. Similarly, [`DockAccessory.FramingMode.left`](dockaccessory/framingmode-swift.enum/left.md) and [`DockAccessory.FramingMode.right`](dockaccessory/framingmode-swift.enum/right.md) aligns the subject close to the left and right third of the frame (left, center, right).

## Topics

### Defining the framing mode
- [DockAccessory.FramingMode.automatic](dockaccessory/framingmode-swift.enum/automatic.md)
  Automatically frame the subject.
- [DockAccessory.FramingMode.center](dockaccessory/framingmode-swift.enum/center.md)
  Frame the subject in the center of the frame.
- [DockAccessory.FramingMode.left](dockaccessory/framingmode-swift.enum/left.md)
  Frame the subject in the left side of the frame.
- [DockAccessory.FramingMode.right](dockaccessory/framingmode-swift.enum/right.md)
  Frame the subject in the right side of the frame.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setFramingMode(DockAccessory.FramingMode) async throws](dockaccessory/setframingmode(_:).md)
  Customize the dock accessory’s tracking behavior.
- [var framingMode: DockAccessory.FramingMode](dockaccessory/framingmode-swift.property.md)
  The current framing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/framingmode-swift.enum)*