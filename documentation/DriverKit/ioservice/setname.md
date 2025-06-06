# SetName

**Framework**: DriverKit  
**Kind**: method

Sets the name of the service in the system’s registry.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetName(const IOServiceName name);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

## Parameters

- `name`: The new name for the service. This method copies the string you provide.

## See Also

- [RegisterService](ioservice/registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [GetRegistryEntryID](ioservice/getregistryentryid.md)
  Returns the registry ID for the current service.
- [IOServiceName](ioservicename.md)
  A string type for setting the name of the service in the system’s registry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/setname)*