# newDeviceDescription

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a new dictionary that describes the HID device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual OSDictionary * newDeviceDescription();
```

#### Return Value

An `OSDictionary` that describes the device.

#### Discussion

This method uses the information from the USB device to create and return the dictionary of attributes. The dictionary always includes the following keys:

- [`kIOHIDReportIntervalKey`](../../iokit/kiohidreportintervalkey.md)
- [`kIOHIDVendorIDKey`](../../iokit/kiohidvendoridkey.md)
- [`kIOHIDProductIDKey`](../../iokit/kiohidproductidkey.md)
- [`kIOHIDTransportKey`](../../iokit/kiohidtransportkey.md)
- [`kIOHIDVersionNumberKey`](../../iokit/kiohidversionnumberkey.md)
- [`kIOHIDCountryCodeKey`](../../iokit/kiohidcountrycodekey.md)
- `kIOHIDRequestTimeoutKey`

The dictionary may also contain some or all of the following keys:

- [`kIOHIDLocationIDKey`](../../iokit/kiohidlocationidkey.md)
- [`kIOHIDManufacturerKey`](../../iokit/kiohidmanufacturerkey.md)
- [`kIOHIDProductKey`](../../iokit/kiohidproductkey.md)
- [`kIOHIDSerialNumberKey`](../../iokit/kiohidserialnumberkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/newdevicedescription)*