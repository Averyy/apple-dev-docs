# digitalCrownAccessory(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func digitalCrownAccessory(_ visibility: Visibility) -> some View
```

## Discussion

Use this method to customize the visibility of a Digital Crown accessory `View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You may want to keep an accessory visible even when the Digital Crown Indicator is not visible to indicate what scrolling the crown will do.

## Parameters

- `visibility`: The visibility of the digital crown accessory.

## See Also

### Interacting with the Digital Crown
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](./digitalcrownaccessory%28content%29.md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./digitalcrownrotation%28_,from,through,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./digitalcrownrotation%28_,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](./digitalcrownrotation%28detent,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](./digitalcrownrotation%28_%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](./digitalcrownrotation%28_,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [struct DigitalCrownEvent](../digitalcrownevent.md)
  An event emitted when the user rotates the Digital Crown.
- [enum DigitalCrownRotationalSensitivity](../digitalcrownrotationalsensitivity.md)
  The amount of Digital Crown rotation needed to move between two integer numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/digitalcrownaccessory(_:))*