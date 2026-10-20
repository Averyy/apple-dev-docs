# right

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) GCControllerButtonInput * right;
```

#### Discussion

The value of the `right` and `left` buttons are mutually exclusive because the user can only press one of these buttons at a time. Therefore, when the `right` button is nonzero, the `left` button is `0`.

## See Also

### Accessing values using directional buttons
- [var left: GCControllerButtonInput](./left.md)
  The button element that changes the negative x-axis.
- [var up: GCControllerButtonInput](./up.md)
  The button element that changes the positive y-axis.
- [var down: GCControllerButtonInput](./down.md)
  The button element used for the negative y-axis direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/right)*