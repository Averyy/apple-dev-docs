# InterruptOccurred

**Framework**: DriverKit  
**Kind**: method

Executes custom code when an interrupt occurs.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void InterruptOccurred(OSAction * action, uint64_t count, uint64_t time);
```

#### Discussion

Use this method as a prototype for declaring your own custom interrupt handlers. When declaring your method, use the [`TYPE`](type.md) macro to indicate that your method has the same parameters and return value as this method.

Use the implementation of your method to respond to any interrupts that occurred.

## Parameters

- `action`: The action object that handles the interrupt event.
- `count`: The number of interrupts that occurred.
- `time`: The time at which the interrupt occurred. The system collects this value using the   function.

## See Also

- [CheckForWork](iointerruptdispatchsource/checkforwork.md)
  Checks for events to handle.
- [IOInterruptDispatchSourcePayload](iointerruptdispatchsourcepayload.md)
  A private structure for an interrupt dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iointerruptdispatchsource/interruptoccurred)*