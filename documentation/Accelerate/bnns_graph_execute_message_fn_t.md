# bnns_graph_execute_message_fn_t

**Framework**: Accelerate  
**Kind**: typealias

The graph execute-message logging callback function.

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
typealias bnns_graph_execute_message_fn_t = (BNNSGraphMessageLevel, UnsafePointer<CChar>, UnsafePointer<CChar>?, UnsafeMutablePointer<bnns_user_message_data_t>?) -> Void
```

## See Also

- [func BNNSGraphContextSetMessageLogCallback(bnns_graph_context_t, bnns_graph_execute_message_fn_t, UnsafeMutablePointer<bnns_user_message_data_t>?) -> Int32](bnnsgraphcontextsetmessagelogcallback(_:_:_:).md)
  Specifies a customized callback function that reports execution-time messages.
- [struct BNNSGraphMessageLevel](bnnsgraphmessagelevel.md)
  Constants that specify the mask for compile-time messages.
- [struct bnns_user_message_data_t](bnns_user_message_data_t.md)
  Additional user-defined logging argument for message-logging callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_execute_message_fn_t)*