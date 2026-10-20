# isPressed

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user is pressing the button.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isPressed: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPressed) BOOL pressed;
```

#### Discussion

If this property is [`true`](../../Swift/true.md), the user is putting pressure on the button; otherwise, the user isn’t.

For the DualSense, DualShock 4, and Siri Remote controllers, the framework simulates whether the user presses the button and the level of pressure for its touch surfaces.

## See Also

### Accessing input values
- [var isTouched: Bool](./istouched.md)
  A Boolean value that indicates whether the user is touching the button.
- [var value: Float](./value.md)
  The level of pressure the user is applying to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/ispressed)*