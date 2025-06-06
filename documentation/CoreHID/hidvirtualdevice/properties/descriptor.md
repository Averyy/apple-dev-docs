# descriptor

**Framework**: Core HID  
**Kind**: property

The HID specification compliant report descriptor for the virtual device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let descriptor: Data
```

## Mentions

- [Creating virtual devices](creatingvirtualdevices.md)

#### Discussion

A report descriptor defines details about the device and the type of interactions that it can have, such as the type of input it can generate, and the queries it responds to. This is the raw descriptor in byte form.

For more details, see [`Human Interface Devices (HID) Specifications and Tools`](https://developer.apple.comhttps://www.usb.org/hid).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/descriptor)*