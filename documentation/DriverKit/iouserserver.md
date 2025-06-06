# IOUserServer

**Framework**: DriverKit  
**Kind**: class

A system-managed service.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOUserServer;
```

#### Overview

You do not create or use instances of this class directly. The system creates them to manage individual services.

## Topics

### Configuring the User Server
- [Create](iouserserver/create.md)
- [init](iouserserver/init.md)
- [free](iouserserver/free.md)
### Managing the Server Lifecycle
- [LoadModule](iouserserver/loadmodule.md)
- [Exit](iouserserver/exit.md)
### Instance Methods
- [RegisterService](iouserserver/registerservice.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOUserClient](iouserclient.md)
  A connection to another service that the system manages.
- [com.apple.developer.driverkit.userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [Communicating between a DriverKit extension and a client app](communicating-between-a-driverkit-extension-and-a-client-app.md)
  Send and receive different kinds of data securely by validating inputs and asynchronously by storing and using a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserserver)*