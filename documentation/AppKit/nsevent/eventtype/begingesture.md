# NSEvent.EventType.beginGesture

**Framework**: AppKit  
**Kind**: case

An event marking the beginning of a gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case beginGesture
```

#### Discussion

Note that apps that link against macOS 10.11 and later no longer receive this event type. If you need to access the phases of a specific gesture, you can implement the responder for that gesture and examine its [`phase`](nsevent/phase-swift.property.md) property instead.

## See Also

- [NSEvent.EventType.endGesture](nsevent/eventtype/endgesture.md)
  An event that marks the end of a gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventtype/begingesture)*