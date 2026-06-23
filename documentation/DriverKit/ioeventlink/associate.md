# Associate

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Associate(uint64_t options);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Associate a thread with the eventlink.

The eventlink should be activated before this call. This is not real-time safe.

## Parameters

- `options`: Options for Associate(). Use kIOEventLinkAssociateCurrentThread or kIOEventLinkAssociateOnWait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink/associate)*