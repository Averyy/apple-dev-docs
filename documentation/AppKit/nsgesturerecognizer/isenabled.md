# isEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the gesture recognizer is able to handle events.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the gesture recognizer receives events and uses them to determine when its gesture is performed. When the value is [`false`](../../Swift/false.md), the gesture recognizer does not receive events. Changing the value from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md) while the gesture recognizer is in the process of recognizing a gesture changes the state of the gesture recognizer to [`NSGestureRecognizer.State.cancelled`](./state-swift.enum/cancelled.md).

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Accessing the recognizer’s state
- [var state: NSGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
- [var view: NSView?](./view.md)
  The view to which the gesture recognizer is attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/isenabled)*