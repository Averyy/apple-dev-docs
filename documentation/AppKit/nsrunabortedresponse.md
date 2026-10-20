# NSRunAbortedResponse

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Modal session was broken with [`abortModal()`](./nsapplication/abortmodal%28%29.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`abort`](./nsapplication/modalresponse/abort.md) instead.

## Declaration

```swift
var NSRunAbortedResponse: Int { get }
```

```c
NSRunAbortedResponse
```

## See Also

### Constants
- [var NSRunContinuesResponse: Int](./nsruncontinuesresponse.md)
  Modal session is continuing (returned by [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md) only).
- [var NSRunStoppedResponse: Int](./nsrunstoppedresponse.md)
  Modal session was broken with [`stopModal()`](./nsapplication/stopmodal%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunabortedresponse)*