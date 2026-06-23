# Invalidate

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Invalidate();
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Invalidate the IOEventLink.

This releases the kernel reference to the IOEventLink, allowing the name to be used for a different IOEventLink. This method should be called after the client has configured the eventlink with the IOConnectTrap call. After invalidation, the IOEventLink can no longer be configured through the IOConnectTrap call. No other functionality is affected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink/invalidate)*