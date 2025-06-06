# BNNSGraphCompileOptionsSetMessageLogCallback(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Specifies a customized callback function that reports compile-time messages.

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
func BNNSGraphCompileOptionsSetMessageLogCallback(_ options: bnns_graph_compile_options_t, _ log_callback: bnns_graph_compile_message_fn_t, _ additional_logging_arguments: UnsafeMutablePointer<bnns_user_message_data_t>?)
```

#### Discussion

If you don’t specify this callback, default callback functions log messages to [`os_log`](https://developer.apple.com/documentation/os/os_log).

The following code adds a custom graph compile message callback function that prints [`BNNSGraphMessageLevelInfo`](bnnsgraphmessagelevelinfo.md) level messages to the console:

```swift
let options = BNNSGraphCompileOptionsMakeDefault()
defer {
    BNNSGraphCompileOptionsDestroy(options)
}

BNNSGraphCompileOptionsSetMessageLogMask(options, BNNSGraphMessageLevelInfo.rawValue)
BNNSGraphCompileOptionsSetMessageLogCallback(options, messageLogCallback, nil)

func messageLogCallback(msg_level: BNNSGraphMessageLevel,
                        error_msg: UnsafePointer<CChar>,
                        source_location: UnsafePointer<CChar>?,
                        user_message_data_t:UnsafeMutablePointer<user_message_data_t>?) {
    
    print(NSString(cString: error_msg, encoding: NSUTF8StringEncoding) ?? "")
    if let source_location = source_location {
        print(NSString(cString: source_location, encoding: NSUTF8StringEncoding) ?? "")
    }
}
```

## Parameters

- `options`: The compilation options object.
- `log_callback`: The message-logging callback function.
- `additional_logging_arguments`: Additional data for the message-logging functions that BNNS passes unaltered to the callback function.

## See Also

- [func BNNSGraphCompileOptionsSetMessageLogMask(bnns_graph_compile_options_t, UInt32)](bnnsgraphcompileoptionssetmessagelogmask(_:_:).md)
  Sets the mask for compile-time messages.
- [func BNNSGraphContextSetMessageLogMask(bnns_graph_context_t, UInt32) -> Int32](bnnsgraphcontextsetmessagelogmask(_:_:).md)
  Sets mask for log messages that are logged (either via `os_log` or the user specified callback)
- [struct BNNSGraphMessageLevel](bnnsgraphmessagelevel.md)
  Constants that specify the mask for compile-time messages.
- [typealias bnns_graph_compile_message_fn_t](bnns_graph_compile_message_fn_t.md)
  The graph compile-message logging callback function.
- [struct bnns_user_message_data_t](bnns_user_message_data_t.md)
  Additional user-defined logging argument for message-logging callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcompileoptionssetmessagelogcallback(_:_:_:))*