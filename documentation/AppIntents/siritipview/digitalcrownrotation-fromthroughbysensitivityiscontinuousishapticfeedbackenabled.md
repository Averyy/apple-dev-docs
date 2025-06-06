# digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)

**Framework**: App Intents  
**Kind**: method

Tracks Digital Crown rotations by updating the specified binding.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
nonisolated
func digitalCrownRotation<V>(_ binding: Binding<V>, from minValue: V, through maxValue: V, by stride: V.Stride? = nil, sensitivity: DigitalCrownRotationalSensitivity = .high, isContinuous: Bool = false, isHapticFeedbackEnabled: Bool = true) -> some View where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

#### Discussion

Use this method to receive values on a binding you provides as the user turns the Digital Crown on Apple Watch. The example below receives changes to the binding value, starting at the `minValue` of  `0.0`  up to the `maxValue` of `10.0` in steps of `0.1` incrementing or decrementing depending on the direction that the user turns the Digital Crown, rolling over if the user exceeds the specified boundary values:

```swift
struct DigitalCrown: View {
    @State private var crownValue = 0.0
    @State private var minValue = 0.0
    @State private var maxValue = 10.0
    @State private var stepAmount = 0.1

    var body: some View {
        Text("Received Value:\(crownValue, specifier: "%.2f")")
            .focusable()
            .digitalCrownRotation($crownValue,
                                  from: minValue,
                                  through: maxValue,
                                  by: stepAmount,
                                  sensitivity: .low,
                                  isContinuous: true)
    }
}
```

## Parameters

- `binding`: A binding to a value that updates when the user rotates   the  Digital Crown.
- `minValue`: Lower end of the range reported.
- `maxValue`: Upper end of the range reported.
- `stride`: The value settles on multiples of  .
- `sensitivity`: How much the user needs to rotate the  Digital Crown   to move between two integer numbers.
- `isContinuous`: Controls if the value reported stops at    and  , or if it should wrap around. Default is  .
- `isHapticFeedbackEnabled`: Controls the generation of haptic feedback   when turning the Digital Crown. Default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/digitalcrownrotation(_:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:))*