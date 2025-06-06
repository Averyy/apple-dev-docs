# IOUserClass

**Framework**: Bundle Resources  
**Kind**: typealias

The name of your driver’s main class, which is the entry point for interacting with your driver’s code.

**Availability**:
- macOS 10.14+

#### Discussion

Include this key only in the personality dictionary of a DriverKit extension, and use it to specify the name of the custom [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass that provides your driver’s behavior. When it’s time to load your driver, the system instantiates the specified class and begins the initialization and startup processes.

## See Also

- [IOProviderClass](information-property-list/ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOClass](information-property-list/ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserClientClass](information-property-list/iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](information-property-list/iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/iouserclass)*