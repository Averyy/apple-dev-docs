# IOServiceName

**Framework**: DriverKit  
**Kind**: typealias

A string type for setting the name of the service in the system’s registry.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef char[128] IOServiceName;
```

## See Also

- [RegisterService](ioservice/registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [SetName](ioservice/setname.md)
  Sets the name of the service in the system’s registry.
- [GetRegistryEntryID](ioservice/getregistryentryid.md)
  Returns the registry ID for the current service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservicename)*