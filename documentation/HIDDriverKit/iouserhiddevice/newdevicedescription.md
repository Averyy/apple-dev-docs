# newDeviceDescription

**Framework**: HIDDriverKit  
**Kind**: method

Creates and returns a new dictionary that describes the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
OSDictionary * newDeviceDescription();
```

#### Return Value

An `OSDictionary` that describes the device.

#### Discussion

Override this method and return a dictionary of key-value pairs that describe the device. The supported keys are:

- [`kIOHIDReportIntervalKey`](https://developer.apple.com/documentation/iokit/kiohidreportintervalkey)
- [`kIOHIDVendorIDKey`](https://developer.apple.com/documentation/iokit/kiohidvendoridkey)
- [`kIOHIDProductIDKey`](https://developer.apple.com/documentation/iokit/kiohidproductidkey)
- [`kIOHIDTransportKey`](https://developer.apple.com/documentation/iokit/kiohidtransportkey)
- [`kIOHIDVersionNumberKey`](https://developer.apple.com/documentation/iokit/kiohidversionnumberkey)
- [`kIOHIDCountryCodeKey`](https://developer.apple.com/documentation/iokit/kiohidcountrycodekey)
- [`kIOHIDLocationIDKey`](https://developer.apple.com/documentation/iokit/kiohidlocationidkey)
- [`kIOHIDManufacturerKey`](https://developer.apple.com/documentation/iokit/kiohidmanufacturerkey)
- [`kIOHIDProductKey`](https://developer.apple.com/documentation/iokit/kiohidproductkey)
- [`kIOHIDSerialNumberKey`](https://developer.apple.com/documentation/iokit/kiohidserialnumberkey)
- `kIOHIDRequestTimeoutKey`


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice/newdevicedescription)*