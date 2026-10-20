# Activate

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
kern_return_t Activate();
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Activate the event link.

The event link must be activated before it can be signaled or waited on. This is not real-time safe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink/activate)*