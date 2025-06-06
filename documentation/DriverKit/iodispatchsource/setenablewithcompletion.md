# SetEnableWithCompletion

**Framework**: DriverKit  
**Kind**: method

Enables or disables the dispatch source.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetEnableWithCompletion(bool enable, IODispatchSourceCancelHandlerhandler);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

Subclasses must provide an implementation of this method.

## Parameters

- `enable`: A Boolean value that indicates whether to enable or disable the dispatch source. Specify   to enable the timer or   to disable it.
- `handler`: An optional handler block to execute after disabling the dispatch source. The dispatch source calls your handler after any in-flight callbacks finish.

## See Also

- [SetEnable](iodispatchsource/setenable.md)
  Enables or disables the delivery of events to your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource/setenablewithcompletion)*