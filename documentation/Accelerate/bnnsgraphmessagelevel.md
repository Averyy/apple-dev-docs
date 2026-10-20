# BNNSGraphMessageLevel

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that specify the mask for compile-time messages.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSGraphMessageLevel
```

```c
typedef enum { ... } BNNSGraphMessageLevel;
```

## Topics

### Graph message levels
- [init(UInt32)](./bnnsgraphmessagelevel/init%28_%29.md)
  Creates a new instance.
- [init(rawValue: UInt32)](./bnnsgraphmessagelevel/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Instance properties
- [var rawValue: UInt32](./bnnsgraphmessagelevel/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSGraphMessageLevelInfo: BNNSGraphMessageLevel](./bnnsgraphmessagelevelinfo.md)
  A constant that specifies information message types.
- [var BNNSGraphMessageLevelWarning: BNNSGraphMessageLevel](./bnnsgraphmessagelevelwarning.md)
  A constant that specifies warning message types.
- [var BNNSGraphMessageLevelError: BNNSGraphMessageLevel](./bnnsgraphmessagelevelerror.md)
  A constant that specifies error message types.
- [var BNNSGraphMessageLevelUnsupported: BNNSGraphMessageLevel](./bnnsgraphmessagelevelunsupported.md)
  A constant that specifies unsupported function message types.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Specifying a graph’s compile-time message callback
- [func BNNSGraphCompileOptionsSetMessageLogMask(bnns_graph_compile_options_t, UInt32)](./bnnsgraphcompileoptionssetmessagelogmask%28_,_%29.md)
  Sets the mask for compile-time messages.
- [func BNNSGraphContextSetMessageLogMask(bnns_graph_context_t, UInt32) -> Int32](./bnnsgraphcontextsetmessagelogmask%28_,_%29.md)
  Sets mask for log messages that are logged (either via `os_log` or the user specified callback)
- [func BNNSGraphCompileOptionsSetMessageLogCallback(bnns_graph_compile_options_t, bnns_graph_compile_message_fn_t, UnsafeMutablePointer<bnns_user_message_data_t>?)](./bnnsgraphcompileoptionssetmessagelogcallback%28_,_,_%29.md)
  Specifies a customized callback function that reports compile-time messages.
- [typealias bnns_graph_compile_message_fn_t](./bnns_graph_compile_message_fn_t.md)
  The graph compile-message logging callback function.
- [struct bnns_user_message_data_t](./bnns_user_message_data_t.md)
  Additional user-defined logging argument for message-logging callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphmessagelevel)*