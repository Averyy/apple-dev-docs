# Open

**Framework**: PCIDriverKit  
**Kind**: method

Opens a session to the PCI device.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kern_return_t Open(IOService *forClient, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

This method gives the specified [`IOService`](https://developer.apple.com/documentation/driverkit/ioservice) object exclusive access to the PCI device. It also gives the service object access to the PCI device’s configuration and aperture space.

## Parameters

- `forClient`: The service object that is opening the session. Typically, you specify your driver’s custom [`IOService`](https://developer.apple.com/documentation/driverkit/ioservice) object.
- `options`: Additional options for opening the session.

## See Also

- [init](iopcidevice/init.md)
  Initializes the device.
- [Close](iopcidevice/close.md)
  Closes the session to the PCI device.
- [free](iopcidevice/free.md)
  Performs any final cleanup for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/open)*