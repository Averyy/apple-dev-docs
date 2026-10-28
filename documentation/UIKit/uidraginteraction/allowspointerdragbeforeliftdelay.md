# allowsPointerDragBeforeLiftDelay

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
var allowsPointerDragBeforeLiftDelay: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsPointerDragBeforeLiftDelay;
```

## Discussion

When this property is [`true`](../../Swift/true.md), a pointer-initiated drag begins as soon as the pointer crosses the minimum movement threshold, regardless of whether the lift delay has elapsed.

When this property is [`false`](../../Swift/false.md), a pointer-initiated drag waits for the lift delay to elapse before checking whether the pointer has crossed the minimum movement threshold. This matches touch-based drag initiation behavior.

Set this property to [`false`](../../Swift/false.md) in gesture-rich views (such as a canvas) where people also interact frequently with secondary gestures in the same view. This ensures consistent gesture disambiguation regardless of input device.

The default value is [`true`](../../Swift/true.md) in iOS and [`false`](../../Swift/false.md) in macOS.

For touch-based gesture timing, use [`liftBehavior`](./liftbehavior-swift.property.md).

## See Also

### Configuring lift behavior
- [var liftBehavior: UIDragInteraction.LiftBehavior](./liftbehavior-swift.property.md)
  A value that controls the timing behavior for initiating a drag gesture from a touch.
- [UIDragInteraction.LiftBehavior](./liftbehavior-swift.enum.md)
  Constants that determine the lift behavior for a drag interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/allowspointerdragbeforeliftdelay)*