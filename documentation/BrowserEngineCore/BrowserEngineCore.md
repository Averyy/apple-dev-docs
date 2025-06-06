# BrowserEngineCore

**Framework**: BrowserEngineCore  
**Kind**: module

Integrate an alternative browser engine into your web browser app.

**Availability**:
- iOS 17.4+
- iPadOS 18.0+

#### Overview

Use the `BrowserEngineCore` framework to support low-level functions for your alternative browser engine that renders its UI using [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit). For more information on developing web browser apps, see [`Designing your browser architecture`](https://developer.apple.com/documentation/BrowserEngineKit/designing-your-browser-architecture).

## Topics

### Kernel events
- [func be_kevent(Int32, UnsafePointer<kevent>!, Int32, UnsafeMutablePointer<kevent>!, Int32, UInt32) -> Int32](be_kevent(_:_:_:_:_:_:).md)
  Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 32-bit data types.
- [func be_kevent64(Int32, UnsafePointer<kevent64_s>!, Int32, UnsafeMutablePointer<kevent64_s>!, Int32, UInt32) -> Int32](be_kevent64(_:_:_:_:_:_:).md)
  Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 64-bit data types.
- [var BE_KEVENT_NO_FLAGS: Int32](be_kevent_no_flags.md)
  Indicates that no flags are set in a request to receive kernel events.
- [var BE_KEVENT_RETURN_IMMEDIATELY: Int32](be_kevent_return_immediately.md)
  Indicates that a request to receive kernel events needs to return without waiting for events.
### JIT compilation
- [var BE_JIT_WRITE_PROTECT_TAG: Int](be_jit_write_protect_tag.md)
  A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserEngineCore)*