# Create

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static kern_return_t Create(OSString *name, IOUserClient *userClient, IOWorkGroup **workgroup);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Create an IOWorkGroup object. This object is not functional until a workgroup port has been set.

## Parameters

- `name`: Name of the workgroup
- `userClient`: Userclient to create the workgroup in. The DriverKit runtime will retain the userclient, and will release it in Invalidate() or when the IOWorkGroup is freed.
- `workgroup`: Created IOWorkGroup with +1 retain count to be released by the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioworkgroup/create)*