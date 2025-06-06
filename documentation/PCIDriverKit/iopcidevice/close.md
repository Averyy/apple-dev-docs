# Close

**Framework**: PCIDriverKit  
**Kind**: method

Closes the session to the PCI device.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
void Close(IOService * forClient, IOOptionBits options);
```

#### Discussion

This method closes the session previously opened by the object in the `forClient` parameter. The method also turns off the Bus Master Enable and Memory Space Enable bits defined in the command register of the PCI specification.

## Parameters

- `forClient`: The service object that is closing the session. If this object doesn’t have an open session to the device, this method does nothing..
- `options`: Additional options for closing the session.

## See Also

- [init](iopcidevice/init.md)
  Initializes the device.
- [Open](iopcidevice/open.md)
  Opens a session to the PCI device.
- [free](iopcidevice/free.md)
  Performs any final cleanup for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/close)*