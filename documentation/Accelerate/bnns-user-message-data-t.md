# bnns_user_message_data_t

**Framework**: Accelerate  
**Kind**: struct

Additional user-defined logging argument for message-logging callbacks.

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
struct bnns_user_message_data_t
```

## Topics

### Initializers
- [init()](bnns_user_message_data_t/init.md)
- [init(size: Int, data: UnsafeMutableRawPointer?)](bnns_user_message_data_t/init(size:data:).md)
  Creates a logging argument structure from the pointer to the additional logging data.
### Instance Properties
- [var data: UnsafeMutableRawPointer?](bnns_user_message_data_t/data.md)
  A pointer to the additional logging data.
- [var size: Int](bnns_user_message_data_t/size.md)
  The size of the additional logging data.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSGraphCompileOptionsSetMessageLogMask(bnns_graph_compile_options_t, UInt32)](bnnsgraphcompileoptionssetmessagelogmask(_:_:).md)
  Sets the mask for compile-time messages.
- [func BNNSGraphContextSetMessageLogMask(bnns_graph_context_t, UInt32) -> Int32](bnnsgraphcontextsetmessagelogmask(_:_:).md)
  Sets mask for log messages that are logged (either via `os_log` or the user specified callback)
- [struct BNNSGraphMessageLevel](bnnsgraphmessagelevel.md)
  Constants that specify the mask for compile-time messages.
- [func BNNSGraphCompileOptionsSetMessageLogCallback(bnns_graph_compile_options_t, bnns_graph_compile_message_fn_t, UnsafeMutablePointer<bnns_user_message_data_t>?)](bnnsgraphcompileoptionssetmessagelogcallback(_:_:_:).md)
  Specifies a customized callback function that reports compile-time messages.
- [typealias bnns_graph_compile_message_fn_t](bnns_graph_compile_message_fn_t.md)
  The graph compile-message logging callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_user_message_data_t)*