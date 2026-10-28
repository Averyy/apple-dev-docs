# down

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) GCControllerButtonInput * down;
```

## Discussion

The value of the `up` and `down` buttons are mutually exclusive because the user can only press one of these buttons at a time. Therefore, when the `down` button is nonzero, the `up` button is `0`.

## See Also

### Accessing values using directional buttons
- [var right: GCControllerButtonInput](./right.md)
  The button element that changes the positive x-axis.
- [var left: GCControllerButtonInput](./left.md)
  The button element that changes the negative x-axis.
- [var up: GCControllerButtonInput](./up.md)
  The button element that changes the positive y-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/down)*