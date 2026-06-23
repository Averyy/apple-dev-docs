# Disassociate

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Disassociate();
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Disassociate the current thread from the eventlink. This is not real-time safe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink/disassociate)*