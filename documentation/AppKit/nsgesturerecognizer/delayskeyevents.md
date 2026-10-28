# delaysKeyEvents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether key events are delivered only after gesture recognition fails.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var delaysKeyEvents: Bool { get set }
```

```objc
@property BOOL delaysKeyEvents;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), key events are delivered to the target view only after gesture recognition fails. Set this property to [`true`](../../Swift/true.md) to prevent the view from processing events that might be recognized as part of a gesture. Once gesture recognition begins, all types of events are delayed until gesture recognition fails.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Delaying events
- [var delaysPrimaryMouseButtonEvents: Bool](./delaysprimarymousebuttonevents.md)
  A Boolean value that indicates whether primary mouse button events are delivered only after gesture recognition fails.
- [var delaysSecondaryMouseButtonEvents: Bool](./delayssecondarymousebuttonevents.md)
  A Boolean value that indicates whether secondary mouse button events are delivered only after gesture recognition fails.
- [var delaysOtherMouseButtonEvents: Bool](./delaysothermousebuttonevents.md)
  A Boolean value that indicates whether other mouse button events are delivered only after gesture recognition fails.
- [var delaysMagnificationEvents: Bool](./delaysmagnificationevents.md)
  A Boolean value that indicates whether magnification events are delivered only after gesture recognition fails.
- [var delaysRotationEvents: Bool](./delaysrotationevents.md)
  A Boolean value that indicates whether rotation events are delivered only after gesture recognition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/delayskeyevents)*