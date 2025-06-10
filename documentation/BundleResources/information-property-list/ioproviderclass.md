# IOProviderClass

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the class that your driver expects to provide the implementation for its provider object.

**Availability**:
- macOS 10.0+

#### Discussion

The value of this key is a string that contains the name of an [`IOService`](https://developer.apple.comhttps://developer.apple.com/documentation/kernel/ioservice-1g) subclass. This class corresponds to the provider object that the system passes to your [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass at startup. (For a kernel extension, the system passes the provider object to the [`start`](https://developer.apple.com/documentation/kernel/ioservice/1532606-start) method of your [`IOService`](https://developer.apple.comhttps://developer.apple.com/documentation/kernel/ioservice-1g) subclass. For a DriverKit extension, the system passes it to the [`Start`](https://developer.apple.com/documentation/DriverKit/IOService/Start) method of your [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass.) Use the provider object in your driver you receive to communicate with the underlying device.

## See Also

- [IOUserClass](information-property-list/iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOClass](information-property-list/ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserClientClass](information-property-list/iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](information-property-list/iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ioproviderclass)*