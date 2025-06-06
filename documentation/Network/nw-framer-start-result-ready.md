# nw_framer_start_result_ready

**Framework**: Network  
**Kind**: var

The protocol is immediately ready to send and receive data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var nw_framer_start_result_ready: nw_framer_start_result_t { get }
```

## See Also

- [var nw_framer_start_result_will_mark_ready: nw_framer_start_result_t](nw_framer_start_result_will_mark_ready.md)
  The protocol will perform a handshake, preventing the overall connection from becoming ready until [`nw_framer_mark_ready(_:)`](nw_framer_mark_ready(_:).md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_start_result_ready)*