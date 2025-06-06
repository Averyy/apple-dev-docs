# delaysOtherMouseButtonEvents

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether other mouse button events are delivered only after gesture recognition fails.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var delaysOtherMouseButtonEvents: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), other mouse button events are delivered to the target view only after gesture recognition fails. Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to prevent the view from processing events that might be recognized as part of a gesture. Once gesture recognition begins, all types of events are delayed until gesture recognition fails.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var delaysPrimaryMouseButtonEvents: Bool](nsgesturerecognizer/delaysprimarymousebuttonevents.md)
  A Boolean value that indicates whether primary mouse button events are delivered only after gesture recognition fails.
- [var delaysSecondaryMouseButtonEvents: Bool](nsgesturerecognizer/delayssecondarymousebuttonevents.md)
  A Boolean value that indicates whether secondary mouse button events are delivered only after gesture recognition fails.
- [var delaysKeyEvents: Bool](nsgesturerecognizer/delayskeyevents.md)
  A Boolean value that indicates whether key events are delivered only after gesture recognition fails.
- [var delaysMagnificationEvents: Bool](nsgesturerecognizer/delaysmagnificationevents.md)
  A Boolean value that indicates whether magnification events are delivered only after gesture recognition fails.
- [var delaysRotationEvents: Bool](nsgesturerecognizer/delaysrotationevents.md)
  A Boolean value that indicates whether rotation events are delivered only after gesture recognition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/delaysothermousebuttonevents)*