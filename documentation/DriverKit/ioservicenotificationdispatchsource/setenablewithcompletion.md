# SetEnableWithCompletion

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t SetEnableWithCompletion(bool enable, IODispatchSourceCancelHandler handler);
```

#### Return Value

kIOReturnSuccess on success. See `IOReturn.h` for error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservicenotificationdispatchsource/setenablewithcompletion)*