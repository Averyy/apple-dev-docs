# DigitalCrownRotationalSensitivity

**Framework**: SwiftUI  
**Kind**: enum

The amount of Digital Crown rotation needed to move between two integer numbers.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum DigitalCrownRotationalSensitivity
```

#### Overview

You may need to experiment to find the level of sensitivity that works for your use case.

## Topics

### Getting sensitivity options
- [DigitalCrownRotationalSensitivity.low](digitalcrownrotationalsensitivity/low.md)
  Low sensitivity.
- [DigitalCrownRotationalSensitivity.medium](digitalcrownrotationalsensitivity/medium.md)
  Medium sensitivity.
- [DigitalCrownRotationalSensitivity.high](digitalcrownrotationalsensitivity/high.md)
  High sensitivity.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func digitalCrownAccessory(Visibility) -> some View](view/digitalcrownaccessory(_:).md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](view/digitalcrownaccessory(content:).md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](view/digitalcrownrotation(_:from:through:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](view/digitalcrownrotation(_:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](view/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](view/digitalcrownrotation(_:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](view/digitalcrownrotation(_:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [struct DigitalCrownEvent](digitalcrownevent.md)
  An event emitted when the user rotates the Digital Crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/digitalcrownrotationalsensitivity)*