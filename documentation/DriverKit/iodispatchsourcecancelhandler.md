# IODispatchSourceCancelHandler

**Framework**: DriverKit  
**Kind**: typealias

A block to execute when a canceled dispatch source stops executing tasks.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (^)(void) IODispatchSourceCancelHandler;
```

## See Also

- [SetEnableWithCompletion](iointerruptdispatchsource/setenablewithcompletion.md)
  Enables or disables the delivery of interrupts.
- [Cancel](iointerruptdispatchsource/cancel.md)
  Cancels all callbacks from the event source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsourcecancelhandler)*