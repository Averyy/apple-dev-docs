# Create

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static kern_return_t Create(OSDictionary *matching, uint64_t options, IODispatchQueue *queue, IOServiceNotificationDispatchSource **notification);
```

## Return Value

kIOReturnSuccess on success. See `IOReturn.h` for error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservicenotificationdispatchsource/create)*