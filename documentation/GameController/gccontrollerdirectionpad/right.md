# right

**Framework**: Game Controller  
**Kind**: property

The button element that changes the positive x-axis.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var right: GCControllerButtonInput { get }
```

#### Discussion

The value of the `right` and `left` buttons are mutually exclusive because the user can only press one of these buttons at a time. Therefore, when the `right` button is nonzero, the `left` button is `0`.

## See Also

- [var left: GCControllerButtonInput](gccontrollerdirectionpad/left.md)
  The button element that changes the negative x-axis.
- [var up: GCControllerButtonInput](gccontrollerdirectionpad/up.md)
  The button element that changes the positive y-axis.
- [var down: GCControllerButtonInput](gccontrollerdirectionpad/down.md)
  The button element used for the negative y-axis direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/right)*