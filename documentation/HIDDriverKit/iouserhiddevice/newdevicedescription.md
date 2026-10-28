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

## Return Value

An `OSDictionary` that describes the device.

## Discussion

Override this method and return a dictionary of key-value pairs that describe the device. The supported keys are:

- [`kIOHIDReportIntervalKey`](../../iokit/kiohidreportintervalkey.md)
- [`kIOHIDVendorIDKey`](../../iokit/kiohidvendoridkey.md)
- [`kIOHIDProductIDKey`](../../iokit/kiohidproductidkey.md)
- [`kIOHIDTransportKey`](../../iokit/kiohidtransportkey.md)
- [`kIOHIDVersionNumberKey`](../../iokit/kiohidversionnumberkey.md)
- [`kIOHIDCountryCodeKey`](../../iokit/kiohidcountrycodekey.md)
- [`kIOHIDLocationIDKey`](../../iokit/kiohidlocationidkey.md)
- [`kIOHIDManufacturerKey`](../../iokit/kiohidmanufacturerkey.md)
- [`kIOHIDProductKey`](../../iokit/kiohidproductkey.md)
- [`kIOHIDSerialNumberKey`](../../iokit/kiohidserialnumberkey.md)
- `kIOHIDRequestTimeoutKey`


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice/newdevicedescription)*