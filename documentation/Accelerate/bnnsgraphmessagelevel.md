# BNNSGraphMessageLevel

**Framework**: Accelerate  
**Kind**: struct

Constants that specify the mask for compile-time messages.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSGraphMessageLevel
```

## Topics

### Graph message levels
- [init(UInt32)](bnnsgraphmessagelevel/init(_:).md)
  Creates a new instance.
- [init(rawValue: UInt32)](bnnsgraphmessagelevel/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance properties
- [var rawValue: UInt32](bnnsgraphmessagelevel/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSGraphMessageLevelInfo: BNNSGraphMessageLevel](bnnsgraphmessagelevelinfo.md)
  A constant that specifies information message types.
- [var BNNSGraphMessageLevelWarning: BNNSGraphMessageLevel](bnnsgraphmessagelevelwarning.md)
  A constant that specifies warning message types.
- [var BNNSGraphMessageLevelError: BNNSGraphMessageLevel](bnnsgraphmessagelevelerror.md)
  A constant that specifies error message types.
- [var BNNSGraphMessageLevelUnsupported: BNNSGraphMessageLevel](bnnsgraphmessagelevelunsupported.md)
  A constant that specifies unsupported function message types.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func BNNSGraphCompileOptionsSetMessageLogMask(bnns_graph_compile_options_t, UInt32)](bnnsgraphcompileoptionssetmessagelogmask(_:_:).md)
  Sets the mask for compile-time messages.
- [func BNNSGraphContextSetMessageLogMask(bnns_graph_context_t, UInt32) -> Int32](bnnsgraphcontextsetmessagelogmask(_:_:).md)
  Sets mask for log messages that are logged (either via `os_log` or the user specified callback)
- [func BNNSGraphCompileOptionsSetMessageLogCallback(bnns_graph_compile_options_t, bnns_graph_compile_message_fn_t, UnsafeMutablePointer<bnns_user_message_data_t>?)](bnnsgraphcompileoptionssetmessagelogcallback(_:_:_:).md)
  Specifies a customized callback function that reports compile-time messages.
- [typealias bnns_graph_compile_message_fn_t](bnns_graph_compile_message_fn_t.md)
  The graph compile-message logging callback function.
- [struct bnns_user_message_data_t](bnns_user_message_data_t.md)
  Additional user-defined logging argument for message-logging callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphmessagelevel)*