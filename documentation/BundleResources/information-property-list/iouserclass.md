# IOUserClass

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of your driver’s main class, which is the entry point for interacting with your driver’s code.

**Availability**:
- macOS 10.14+

## Details

- **Name**: `IOUserClass`
- **Type**: string

## Discussion

Include this key only in the personality dictionary of a DriverKit extension, and use it to specify the name of the custom [`IOService`](../../DriverKit/ioservice.md) subclass that provides your driver’s behavior. When it’s time to load your driver, the system instantiates the specified class and begins the initialization and startup processes.

## See Also

### Driver Classes
- [IOProviderClass](./ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOClass](./ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserClientClass](./iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](./iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/iouserclass)*