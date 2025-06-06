# RegisterService

**Framework**: DriverKit  
**Kind**: method

Starts the registration process for the service and performs any additional matching.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t RegisterService();
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

After setting up your service in your custom [`Start`](ioservice/start.md) method, call this method to let the system know your service is running.

## See Also

- [SetName](ioservice/setname.md)
  Sets the name of the service in the system’s registry.
- [GetRegistryEntryID](ioservice/getregistryentryid.md)
  Returns the registry ID for the current service.
- [IOServiceName](ioservicename.md)
  A string type for setting the name of the service in the system’s registry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/registerservice)*