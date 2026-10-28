# Open

**Framework**: PCIDriverKit  
**Kind**: method  
**Role**: Instance Method

Opens a session to the PCI device.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
kern_return_t Open(IOService *forClient, IOOptionBits options);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

This method gives the specified [`IOService`](../../DriverKit/ioservice.md) object exclusive access to the PCI device. It also gives the service object access to the PCI device’s configuration and aperture space.

## Parameters

- `forClient`: The service object that is opening the session. Typically, you specify your driver’s custom [`IOService`](../../DriverKit/ioservice.md) object.
- `options`: Additional options for opening the session.

## See Also

### Running the Service
- [init](./init.md)
  Initializes the device.
- [Close](./close.md)
  Closes the session to the PCI device.
- [free](./free.md)
  Performs any final cleanup for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/open)*