# digitalCrownRotation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Tracks Digital Crown rotations by updating the specified binding.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
func digitalCrownRotation<V>(_ binding: Binding<V>) -> some View where V : BinaryFloatingPoint
```

## Discussion

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

![A screenshot showing a value received by turning the Digital Crown](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-digitalCrownRotationBinding@2x.png)

## Parameters

- `binding`: A binding to a value that updates as the user rotates the Digital Crown. The implicit range is `(-infinity, +infinity)`.

## See Also

### Interacting with the Digital Crown
- [func digitalCrownAccessory(Visibility) -> some View](./digitalcrownaccessory%28_%29.md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](./digitalcrownaccessory%28content%29.md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./digitalcrownrotation%28_,from,through,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](./digitalcrownrotation%28_,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](./digitalcrownrotation%28detent,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled,onchange,onidle%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](./digitalcrownrotation%28_,from,through,by,sensitivity,iscontinuous,ishapticfeedbackenabled%29.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [struct DigitalCrownEvent](../digitalcrownevent.md)
  An event emitted when the user rotates the Digital Crown.
- [enum DigitalCrownRotationalSensitivity](../digitalcrownrotationalsensitivity.md)
  The amount of Digital Crown rotation needed to move between two integer numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/digitalcrownrotation(_:))*