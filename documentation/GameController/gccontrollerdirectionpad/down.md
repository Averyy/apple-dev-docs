# down

**Framework**: Game Controller  
**Kind**: property

The button element used for the negative y-axis direction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var down: GCControllerButtonInput { get }
```

#### Discussion

The value of the `up` and `down` buttons are mutually exclusive because the user can only press one of these buttons at a time. Therefore, when the `down` button is nonzero, the `up` button is `0`.

## See Also

- [var right: GCControllerButtonInput](gccontrollerdirectionpad/right.md)
  The button element that changes the positive x-axis.
- [var left: GCControllerButtonInput](gccontrollerdirectionpad/left.md)
  The button element that changes the negative x-axis.
- [var up: GCControllerButtonInput](gccontrollerdirectionpad/up.md)
  The button element that changes the positive y-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/down)*