# Join

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Join(void *token);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Join the workgroup.

Before calling this method, the caller must allocate a token. This token must be passed to this method. When leaving a workgroup with Leave(), use the same token that was passed to Join().

## Parameters

- `token`: The workgroup token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioworkgroup/join)*