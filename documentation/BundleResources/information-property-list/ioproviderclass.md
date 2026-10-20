# IOProviderClass

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the class that your driver expects to provide the implementation for its provider object.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `IOProviderClass`
- **Type**: string

#### Discussion

The value of this key is a string that contains the name of an [IOService](../../kernel/ioservice-1g.md) subclass. This class corresponds to the provider object that the system passes to your [`IOService`](../../DriverKit/ioservice.md) subclass at startup. (For a kernel extension, the system passes the provider object to the [`start`](../../kernel/ioservice/api-1532606-start.md) method of your [`IOService`](../../kernel/ioservice-1g.md) subclass. For a DriverKit extension, the system passes it to the [`Start`](../../DriverKit/ioservice/start.md) method of your [`IOService`](../../DriverKit/ioservice.md) subclass.) Use the provider object in your driver you receive to communicate with the underlying device.

## See Also

### Driver Classes
- [IOUserClass](./iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOClass](./ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserClientClass](./iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](./iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ioproviderclass)*