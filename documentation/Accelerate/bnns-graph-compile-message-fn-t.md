# bnns_graph_compile_message_fn_t

**Framework**: Accelerate  
**Kind**: typealias

The graph compile-message logging callback function.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
typealias bnns_graph_compile_message_fn_t = (BNNSGraphMessageLevel, UnsafePointer<CChar>, UnsafePointer<CChar>?, UnsafeMutablePointer<bnns_user_message_data_t>?) -> Void
```

## See Also

- [func BNNSGraphCompileOptionsSetMessageLogMask(bnns_graph_compile_options_t, UInt32)](bnnsgraphcompileoptionssetmessagelogmask(_:_:).md)
  Sets the mask for compile-time messages.
- [func BNNSGraphContextSetMessageLogMask(bnns_graph_context_t, UInt32) -> Int32](bnnsgraphcontextsetmessagelogmask(_:_:).md)
  Sets mask for log messages that are logged (either via `os_log` or the user specified callback)
- [struct BNNSGraphMessageLevel](bnnsgraphmessagelevel.md)
  Constants that specify the mask for compile-time messages.
- [func BNNSGraphCompileOptionsSetMessageLogCallback(bnns_graph_compile_options_t, bnns_graph_compile_message_fn_t, UnsafeMutablePointer<bnns_user_message_data_t>?)](bnnsgraphcompileoptionssetmessagelogcallback(_:_:_:).md)
  Specifies a customized callback function that reports compile-time messages.
- [struct bnns_user_message_data_t](bnns_user_message_data_t.md)
  Additional user-defined logging argument for message-logging callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_compile_message_fn_t)*