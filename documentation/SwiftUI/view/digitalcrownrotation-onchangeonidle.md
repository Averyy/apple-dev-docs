# digitalCrownRotation(_:onChange:onIdle:)

**Framework**: SwiftUI  
**Kind**: method

Tracks Digital Crown rotations by updating the specified binding.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func digitalCrownRotation<V>(_ binding: Binding<V>, onChange: @escaping (DigitalCrownEvent) -> Void = { _ in }, onIdle: @escaping () -> Void = { }) -> some View where V : BinaryFloatingPoint
```

#### Discussion

Use this method to receive values on a binding you provide as the user turns the Digital Crown on Apple Watch. The example below receives changes to the binding value, starting at `0.0` and incrementing or decrementing depending on the direction that the user turns the Digital Crown:

```swift
struct DigitalCrown: View {
    @State private var crownValue = 0.0

    var body: some View {
        Text("Received Value:\(crownValue, specifier: "%.1f")")
            .focusable()
            .digitalCrownRotation($crownValue)
    }
}
```

![A screenshot showing a value received by turning the Digital Crown](https://docs-assets.developer.apple.com/published/e6e83d760dbde075ad17f9f337d50e55/SwiftUI-View-digitalCrownRotationBinding%402x.png)

## Parameters

- `binding`: A binding to a value that updates as the user   rotates the Digital Crown. The implicit range is   .
- `onChange`: A block that is called as the Digital Crown is rotated.
- `onIdle`: A block that is called when the Digital Crown has settled to   an idle state.

## See Also

- [func digitalCrownAccessory(Visibility) -> some View](view/digitalcrownaccessory(_:).md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](view/digitalcrownaccessory(content:).md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](view/digitalcrownrotation(_:from:through:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](view/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](view/digitalcrownrotation(_:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](view/digitalcrownrotation(_:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [struct DigitalCrownEvent](digitalcrownevent.md)
  An event emitted when the user rotates the Digital Crown.
- [enum DigitalCrownRotationalSensitivity](digitalcrownrotationalsensitivity.md)
  The amount of Digital Crown rotation needed to move between two integer numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/digitalcrownrotation(_:onchange:onidle:))*