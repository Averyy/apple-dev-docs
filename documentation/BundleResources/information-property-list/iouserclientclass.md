# IOUserClientClass

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the class to instantiate when the system requires a client connection to the driver.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `IOUserClientClass`
- **Type**: string

## Discussion

The value of this key is a string that contains the name of an [IOService](../../kernel/ioservice.md) subclass in your driver.

## See Also

### Driver Classes
- [IOUserClass](./iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOProviderClass](./ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOClass](./ioclass.md)
  The name of the class to instantiate from your driver.
- [IOUserServerName](./iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/iouserclientclass)*