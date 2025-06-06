# IOUserServerName

**Framework**: Bundle Resources  
**Kind**: typealias

The name that the system uses to facilitate communication between your driver and other clients.

**Availability**:
- macOS 10.14+

#### Discussion

Typically, you set the value of this key to your kext or DriverKit extension’s bundle identifier. The system registers your driver under the specified server name, and uses that name to facilitate communications between your driver and other clients, including the kernel itself.

## See Also

- [IOUserClass](information-property-list/iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOProviderClass](information-property-list/ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOClass](information-property-list/ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserClientClass](information-property-list/iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/iouserservername)*