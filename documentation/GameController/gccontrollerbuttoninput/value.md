# value

**Framework**: Game Controller  
**Kind**: property

The level of pressure the user is applying to the button.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var value: Float { get }
```

#### Discussion

If the user applies pressure to the button, the [`isPressed`](gccontrollerbuttoninput/ispressed.md) property is [`true`](https://developer.apple.com/documentation/swift/true) and this property indicates the amount of pressure. The framework normalizes the value to a number between `0.0` (minimum) and `1.0` (maximum). If the user isn’t pressing the button, the [`isPressed`](gccontrollerbuttoninput/ispressed.md) property is [`false`](https://developer.apple.com/documentation/swift/false) and this property is `0.0`.

For axis buttons, such as thumbsticks and touchpads, the location on the positive or negative axis of the element simulates the pressure.

## See Also

- [var isTouched: Bool](gccontrollerbuttoninput/istouched.md)
  A Boolean value that indicates whether the user is touching the button.
- [var isPressed: Bool](gccontrollerbuttoninput/ispressed.md)
  A Boolean value that indicates whether the user is pressing the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/value)*