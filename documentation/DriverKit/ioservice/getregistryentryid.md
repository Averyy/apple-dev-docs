# GetRegistryEntryID

**Framework**: DriverKit  
**Kind**: method

Returns the registry ID for the current service.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t GetRegistryEntryID(uint64_t * registryEntryID);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

## Parameters

- `registryEntryID`: A pointer to an integer that, on return, contains the registry ID for the service. It is a programmer error to specify   or an invalid pointer for this parameter.

## See Also

- [RegisterService](ioservice/registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [SetName](ioservice/setname.md)
  Sets the name of the service in the system’s registry.
- [IOServiceName](ioservicename.md)
  A string type for setting the name of the service in the system’s registry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/getregistryentryid)*