# Cancel

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
kern_return_t Cancel();
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Cancel the event link.

If a thread is waiting on the eventlink, cancellation will wake up that thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink/cancel)*