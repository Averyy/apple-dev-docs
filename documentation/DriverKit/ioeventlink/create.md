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
static kern_return_t Create(OSString *name, IOUserClient *userClient, IOEventLink **eventLink);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Create an IOEventLink.

## Parameters

- `name`: User-specified name. If an IOEventLink with the same name already exists in the specified user client, the old IOEventLink will be replaced.
- `userClient`: Userclient to create the eventlink in. The DriverKit runtime will retain the userclient, and will release it in Invalidate() or when the IOEventLink is freed.
- `eventLink`: Created IOEventLink with +1 retain count to be released by the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink/create)*