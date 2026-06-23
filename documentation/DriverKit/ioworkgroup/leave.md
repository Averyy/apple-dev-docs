# Leave

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Leave(void *token);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Leave the workgroup.

The workgroup must have been joined with Join(). Use the same token in Join() for this method.

## Parameters

- `token`: The workgroup token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioworkgroup/leave)*