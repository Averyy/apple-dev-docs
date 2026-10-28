# CheckForWork

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Checks for events to handle.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t CheckForWork(bool synchronous);
```

## Return Value

[`kIOReturnSuccess`](../kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../error-codes.md).

## Discussion

Don’t override this method or call it from your own code. The dispatch source uses this method internally to check for events.

## See Also

### Declaring Actions
- [InterruptOccurred](./interruptoccurred.md)
  Executes custom code when an interrupt occurs.
- [IOInterruptDispatchSourcePayload](../iointerruptdispatchsourcepayload.md)
  A private structure for an interrupt dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iointerruptdispatchsource/checkforwork)*