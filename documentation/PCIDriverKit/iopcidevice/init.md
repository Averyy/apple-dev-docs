# init

**Framework**: PCIDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the device.

**Availability**:
- DriverKit
- macOS

## Declaration

```cpp
virtual bool init();
```

#### Return Value

[`true`](../../Swift/true.md) if initialization was successful, or [`false`](../../Swift/false.md) if it was unsuccessful.

## See Also

### Running the Service
- [Open](./open.md)
  Opens a session to the PCI device.
- [Close](./close.md)
  Closes the session to the PCI device.
- [free](./free.md)
  Performs any final cleanup for the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/init)*