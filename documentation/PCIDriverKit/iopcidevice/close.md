# Close

**Framework**: PCIDriverKit  
**Kind**: method  
**Role**: Instance Method

Closes the session to the PCI device.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
void Close(IOService *forClient, IOOptionBits options);
```

## Discussion

This method closes the session previously opened by the object in the `forClient` parameter. The method also turns off the Bus Master Enable and Memory Space Enable bits defined in the command register of the PCI specification.

## Parameters

- `forClient`: The service object that is closing the session. If this object doesn’t have an open session to the device, this method does nothing..
- `options`: Additional options for closing the session.

## See Also

### Running the Service
- [init](./init.md)
  Initializes the device.
- [Open](./open.md)
  Opens a session to the PCI device.
- [free](./free.md)
  Performs any final cleanup for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/close)*