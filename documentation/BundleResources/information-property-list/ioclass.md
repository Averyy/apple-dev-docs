# IOClass

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the class to instantiate from your driver.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `IOClass`
- **Type**: string

## Discussion

The value of this key is a string that contains the name of a custom [IOService](../../kernel/ioservice.md) subclass in your driver. When the system successfully matches one of your driver’s personalities to a device, it instantiates the class in this key and calls its [`start`](../../kernel/ioservice/api-1532606-start.md) method.

For the personalities in a DriverKit extension, specify the value `IOUserService` unless otherwise directed by the documentation. For example, the [`IOUserHIDEventService`](../../HIDDriverKit/iouserhideventservice.md) class expects you to specify the value `AppleUserHIDEventService`.

## See Also

### Driver Classes
- [IOUserClass](./iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOProviderClass](./ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOUserClientClass](./iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](./iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ioclass)*