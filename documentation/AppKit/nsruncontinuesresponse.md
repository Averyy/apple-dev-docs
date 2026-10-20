# NSRunContinuesResponse

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Modal session is continuing (returned by [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md) only).

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`continue`](./nsapplication/modalresponse/continue.md) instead.

## Declaration

```swift
var NSRunContinuesResponse: Int { get }
```

```c
NSRunContinuesResponse
```

## See Also

### Constants
- [var NSRunAbortedResponse: Int](./nsrunabortedresponse.md)
  Modal session was broken with [`abortModal()`](./nsapplication/abortmodal%28%29.md).
- [var NSRunStoppedResponse: Int](./nsrunstoppedresponse.md)
  Modal session was broken with [`stopModal()`](./nsapplication/stopmodal%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruncontinuesresponse)*