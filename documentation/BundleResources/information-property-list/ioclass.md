# IOClass

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the class to instantiate from your driver.

**Availability**:
- macOS 10.0+

#### Discussion

The value of this key is a string that contains the name of a custom [`IOService`](https://developer.apple.comhttps://developer.apple.com/documentation/kernel/ioservice-1g) subclass in your driver. When the system successfully matches one of your driver’s personalities to a device, it instantiates the class in this key and calls its [`start`](https://developer.apple.com/documentation/kernel/ioservice/1532606-start) method.

For the personalities in a DriverKit extension, specify the value `IOUserService` unless otherwise directed by the documentation. For example, the [`IOUserHIDEventService`](https://developer.apple.com/documentation/HIDDriverKit/IOUserHIDEventService) class expects you to specify the value `AppleUserHIDEventService`.

## See Also

- [IOUserClass](information-property-list/iouserclass.md)
  The name of your driver’s main class, which is the entry point for interacting with your driver’s code.
- [IOProviderClass](information-property-list/ioproviderclass.md)
  The name of the class that your driver expects to provide the implementation for its provider object.
- [IOUserClientClass](information-property-list/iouserclientclass.md)
  The name of the class to instantiate when the system requires a client connection to the driver.
- [IOUserServerName](information-property-list/iouserservername.md)
  The name that the system uses to facilitate communication between your driver and other clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ioclass)*