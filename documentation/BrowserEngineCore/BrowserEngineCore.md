# BrowserEngineCore

**Framework**: BrowserEngineCore  
**Kind**: module  
**Role**: Framework

Integrate an alternative browser engine into your web browser app.

**Availability**:
- iOS 17.4+
- iPadOS 18.0+

#### Overview

Use the `BrowserEngineCore` framework to support low-level functions for your alternative browser engine that renders its UI using [BrowserEngineKit](../BrowserEngineKit/BrowserEngineKit.md). For more information on developing web browser apps, see [Designing your browser architecture](../BrowserEngineKit/designing-your-browser-architecture.md).

## Topics

### Kernel events
- [func be_kevent(Int32, UnsafePointer<kevent>!, Int32, UnsafeMutablePointer<kevent>!, Int32, UInt32) -> Int32](./be_kevent%28_,_,_,_,_,_%29.md)
  Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 32-bit data types.
- [func be_kevent64(Int32, UnsafePointer<kevent64_s>!, Int32, UnsafeMutablePointer<kevent64_s>!, Int32, UInt32) -> Int32](./be_kevent64%28_,_,_,_,_,_%29.md)
  Registers for kernel events on the specified queue, and returns events that are pending on the queue, using 64-bit data types.
- [var BE_KEVENT_NO_FLAGS: Int32](./be_kevent_no_flags.md)
  Indicates that no flags are set in a request to receive kernel events.
- [var BE_KEVENT_RETURN_IMMEDIATELY: Int32](./be_kevent_return_immediately.md)
  Indicates that a request to receive kernel events needs to return without waiting for events.
### JIT compilation
- [var BE_JIT_WRITE_PROTECT_TAG: Int](./be_jit_write_protect_tag.md)
  A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.
- [be_memory_inline_jit_restrict_with_witness_supported](./be_memory_inline_jit_restrict_with_witness_supported.md)
  Reports whether write protection for just-in-time (JIT) compilation is available.
- [be_memory_inline_jit_restrict_rwx_to_rw_with_witness](./be_memory_inline_jit_restrict_rwx_to_rw_with_witness.md)
  Makes a region of memory writable for use in just-in-time (JIT) compilation.
- [be_memory_inline_jit_restrict_rwx_to_rx_with_witness](./be_memory_inline_jit_restrict_rwx_to_rx_with_witness.md)
  Makes a region of memory executable for use in just-in-time (JIT) compilation.
### Audio preferences
- [class BEAudioSession](./beaudiosession-7bb2q.md)
  An object that wraps an AV audio session to scope the browser app’s audio session control.
- [class BEAudioSession](./beaudiosession-6b7ig.md)
  An object that wraps an AV audio session to scope the browser app’s audio session control.
### Memory-protection implementation
- [be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl](./be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl.md)
  Makes a region of memory writable for use in just-in-time (JIT) compilation.
- [be_memory_inline_jit_restrict_rwx_to_rx_with_witness_impl](./be_memory_inline_jit_restrict_rwx_to_rx_with_witness_impl.md)
  Makes a region of memory executable for use in just-in-time (JIT) compilation.
### API availability
- [BROWSERENGINE_ACCESSIBILITY_AVAILABILITY](./browserengine_accessibility_availability.md)
  A macro the framework uses to indicate which SDK versions provide the accessibility APIs.
- [BROWSERENGINE_ACCESSIBILITY_MARKER_AVAILABILITY](./browserengine_accessibility_marker_availability.md)
  A macro the framework uses to indicate which SDK versions provide the accessibility marker APIs.
- [BROWSERENGINE_ACCESSIBILITY_REMOTE_AVAILABILITY](./browserengine_accessibility_remote_availability.md)
  A macro that indicates the SDK versions that provide the APIs for accessibility remote elements.
- [BROWSERENGINE_TEXTINPUT_AVAILABILITY](./browserengine_textinput_availability.md)
  A macro the framework uses to indicate which SDK versions provide the text input APIs.
- [BROWSERENGINE_EXPORT](./browserengine_export.md)
  A macro the framework uses to make API available for use in your code.
- [BROWSERENGINE_EXTERN](./browserengine_extern.md)
  A macro the framework uses to indicate that a symbol is defined in a different file.
- [BROWSERENGINE_FINAL](./browserengine_final.md)
  A macro the framework uses to indicate that an Objective-C class isn’t available for subclassing.
- [BROWSERENGINE_IMPORT](./browserengine_import.md)
  A macro the framework uses to import APIs from other frameworks.
### Macros
- [BROWSERENGINE_ACCESSIBILITY_AVAILABILITY_27](./browserengine_accessibility_availability_27.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserEngineCore)*