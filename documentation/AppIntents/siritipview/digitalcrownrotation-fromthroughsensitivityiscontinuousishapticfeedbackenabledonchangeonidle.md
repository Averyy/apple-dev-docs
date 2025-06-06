# digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)

**Framework**: App Intents  
**Kind**: method

Tracks Digital Crown rotations by updating the specified binding.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func digitalCrownRotation<V>(_ binding: Binding<V>, from minValue: V, through maxValue: V, sensitivity: DigitalCrownRotationalSensitivity = .high, isContinuous: Bool = false, isHapticFeedbackEnabled: Bool = true, onChange: @escaping (DigitalCrownEvent) -> Void = { _ in }, onIdle: @escaping () -> Void = { }) -> some View where V : BinaryFloatingPoint
```

#### Discussion

Use this method to receive continuous values on a binding you provides as the user turns the Digital Crown on Apple Watch. The example below receives changes to the binding value, starting at the `minValue` of `0.0`  up to the `maxValue` of `10.0` settling in to multiples of `0.1` increasing or decreasing depending on the direction that the user turns the Digital Crown, rolling over if the user exceeds the specified boundary values:

```swift
struct DigitalCrown: View {
    @State private var crownValue = 0.0
    @State private var minValue = 0.0
    @State private var maxValue = 10.0
    @State private var velocity = 0.0
    @State private var isIdle = true

    var body: some View {
        Text("Received Value:\(crownValue, specifier: "%.2f")")
            .focusable()
            .digitalCrownRotation($crownValue,
                                  from: minValue,
                                  through: maxValue,
                                  sensitivity: .low,
                                  isContinuous: true
            ) { crownEvent in
                isIdle = false
                velocity = crownEvent.velocity
            } onIdle: {
                isIdle = true
            }
    }
}
```

## Parameters

- `binding`: A binding to a value that updates when the user rotates   the  Digital Crown.
- `minValue`: Lower end of the range reported.
- `maxValue`: Upper end of the range reported.
- `sensitivity`: How much the user needs to rotate the  Digital Crown   to move between two integer numbers.
- `isContinuous`: Controls if the value reported stops at    and  , or if it should wrap around. Default is  .
- `isHapticFeedbackEnabled`: Controls the generation of haptic feedback   when turning the Digital Crown. Default is  .
- `onChange`: A block that is called as the Digital Crown is rotated.
- `onIdle`: A block that is called when the Digital Crown has settled to   an idle state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/digitalcrownrotation(_:from:through:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:))*