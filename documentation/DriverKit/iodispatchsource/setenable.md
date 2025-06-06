# SetEnable

**Framework**: DriverKit  
**Kind**: method

Enables or disables the delivery of events to your code.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetEnable(bool enable);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

## Parameters

- `enable`: A Boolean value that indicates whether to enable or disable the dispatch source. Specify   to enable it or   to disable it.

## See Also

- [SetEnableWithCompletion](iodispatchsource/setenablewithcompletion.md)
  Enables or disables the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource/setenable)*