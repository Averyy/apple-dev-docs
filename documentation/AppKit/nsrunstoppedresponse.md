# NSRunStoppedResponse

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Modal session was broken with [`stopModal()`](./nsapplication/stopmodal%28%29.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`stop`](./nsapplication/modalresponse/stop.md) instead.

## Declaration

```swift
var NSRunStoppedResponse: Int { get }
```

```c
NSRunStoppedResponse
```

## See Also

### Constants
- [var NSRunAbortedResponse: Int](./nsrunabortedresponse.md)
  Modal session was broken with [`abortModal()`](./nsapplication/abortmodal%28%29.md).
- [var NSRunContinuesResponse: Int](./nsruncontinuesresponse.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md) only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunstoppedresponse)*