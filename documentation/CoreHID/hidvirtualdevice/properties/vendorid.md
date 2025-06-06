# vendorID

**Framework**: Core HID  
**Kind**: property

The vendor ID for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let vendorID: UInt32
```

## Mentions

- [Creating virtual devices](creatingvirtualdevices.md)

#### Discussion

The vendor ID designates the vendor that produced the device. It can be combined with [`productID`](hidvirtualdevice/properties/productid.md) to determine the exact device.

More information about vendor IDs can be found online. The vendor ID associated with a HID device is typically a [`USB vendor ID`](https://developer.apple.comhttps://www.usb.org/developers), but can be something else, such as a [`Bluetooth vendor ID`](https://developer.apple.comhttps://www.bluetooth.com/specifications/assigned-numbers/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/vendorid)*