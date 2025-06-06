# BNNSGraphContextSetMessageLogCallback(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies a customized callback function that reports execution-time messages.

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
func BNNSGraphContextSetMessageLogCallback(_ context: bnns_graph_context_t, _ log_callback_fn: bnns_graph_execute_message_fn_t, _ additional_logging_arguments: UnsafeMutablePointer<bnns_user_message_data_t>?) -> Int32
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

The following code adds a custom context execute-message callback function that prints messages to the console:

```swift
BNNSGraphContextSetMessageLogCallback(context, messageLogCallback, nil)

func messageLogCallback(msg_level: BNNSGraphMessageLevel,
                        error_msg: UnsafePointer<CChar>,
                        op_info: UnsafePointer<CChar>?,
                        additional_logging_arguments: UnsafeMutablePointer<user_message_data_t>?) {

    print(NSString(cString: error_msg, encoding: NSUTF8StringEncoding) ?? "")
    if let op_info = op_info {
        print(NSString(cString: op_info, encoding: NSUTF8StringEncoding) ?? "")
    }
}
```

## Parameters

- `context`: The graph context.
- `log_callback_fn`: The message-logging callback function.
- `additional_logging_arguments`: Additional data for the message logging functions that BNNS passes unaltered to the callback function.

## See Also

- [typealias bnns_graph_execute_message_fn_t](bnns_graph_execute_message_fn_t.md)
  The graph execute-message logging callback function.
- [struct BNNSGraphMessageLevel](bnnsgraphmessagelevel.md)
  Constants that specify the mask for compile-time messages.
- [struct bnns_user_message_data_t](bnns_user_message_data_t.md)
  Additional user-defined logging argument for message-logging callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextsetmessagelogcallback(_:_:_:))*