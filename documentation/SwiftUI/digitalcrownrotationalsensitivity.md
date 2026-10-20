# DigitalCrownRotationalSensitivity

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [DigitalCrownRotationalSensitivity.low](./digitalcrownrotationalsensitivity/low.md)
  Low sensitivity.
- [DigitalCrownRotationalSensitivity.medium](./digitalcrownrotationalsensitivity/medium.md)
  Medium sensitivity.
- [DigitalCrownRotationalSensitivity.high](./digitalcrownrotationalsensitivity/high.md)
  High sensitivity.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interacting with the Digital Crown
- [func digitalCrownAccessory(Visibility) -> some View](./view/digitalcrownaccessory%28_%29.md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](./view/digitalcrownaccessory%28content%29.md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./view/digitalcrownrotation%28_,from,through,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./view/digitalcrownrotation%28_,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](./view/digitalcrownrotation%28detent,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](./view/digitalcrownrotation%28_%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](./view/digitalcrownrotation%28_,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [struct DigitalCrownEvent](./digitalcrownevent.md)
  An event emitted when the user rotates the Digital Crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/digitalcrownrotationalsensitivity)*