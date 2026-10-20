# NSEvent.EventType.beginGesture

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An event marking the beginning of a gesture.

**Availability**:
- macOS 10.5+ - Deprecated in 27.0

> **Deprecated**: NSEventTypeBeginGesture is no longer delivered. Use the phase property on NSEvent or NSGestureRecognizer instead.

## Declaration

```swift
case beginGesture
```

```c
NSEventTypeBeginGesture
```

#### Discussion

Note that apps that link against macOS 10.11 and later no longer receive this event type. If you need to access the phases of a specific gesture, you can implement the responder for that gesture and examine its [`phase`](../phase-swift.property.md) property instead.

## See Also

### Deprecated symbols
- [NSEvent.EventType.endGesture](./endgesture.md)
  An event that marks the end of a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/begingesture)*