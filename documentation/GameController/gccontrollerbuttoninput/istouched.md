# isTouched

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the user is touching the button.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isTouched: Bool { get }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), the user is touching the button; otherwise, the user isn’t. For controllers that support capacitive touch, the user can start touching the button without pressure when the value property is `0`. For controllers that don’t support capacitive touch, the user starts touching the button when the value property is greater than `0`.

## See Also

- [var isPressed: Bool](gccontrollerbuttoninput/ispressed.md)
  A Boolean value that indicates whether the user is pressing the button.
- [var value: Float](gccontrollerbuttoninput/value.md)
  The level of pressure the user is applying to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/istouched)*