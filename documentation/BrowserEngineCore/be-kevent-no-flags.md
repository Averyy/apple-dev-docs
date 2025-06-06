# BE_KEVENT_NO_FLAGS

**Framework**: BrowserEngineCore  
**Kind**: var

Indicates that no flags are set in a request to receive kernel events.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var BE_KEVENT_NO_FLAGS: Int32 { get }
```

#### Discussion

Use this constant in the `be_flags` parameter of [`be_kevent(_:_:_:_:_:_:)`](be_kevent(_:_:_:_:_:_:).md), or the `flags` parameter of [`be_kevent64(_:_:_:_:_:_:)`](be_kevent64(_:_:_:_:_:_:).md).

## See Also

- [func be_kevent(Int32, UnsafePointer<kevent>!, Int32, UnsafeMutablePointer<kevent>!, Int32, UInt32) -> Int32](be_kevent(_:_:_:_:_:_:).md)
  Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 32-bit data types.
- [func be_kevent64(Int32, UnsafePointer<kevent64_s>!, Int32, UnsafeMutablePointer<kevent64_s>!, Int32, UInt32) -> Int32](be_kevent64(_:_:_:_:_:_:).md)
  Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 64-bit data types.
- [var BE_KEVENT_RETURN_IMMEDIATELY: Int32](be_kevent_return_immediately.md)
  Indicates that a request to receive kernel events needs to return without waiting for events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/be_kevent_no_flags)*