# vendorID

**Framework**: Core HID  
**Kind**: property

The vendor ID for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var vendorID: UInt32?
```

#### Discussion

The vendor ID designates the vendor that produced the device. Combine the vendor ID with the [`productID`](hiddevicemanager/devicematchingcriteria/productid.md) to determine the exact device.

More information about vendor IDs can be found online. The vendor ID associated with a HID device is typically a USB vendor ID (see [`Information for Developers`](https://developer.apple.comhttps://www.usb.org/developers)), but can be something else, such as a Bluetooth vendor ID (see [`Assigned Numbers`](https://developer.apple.comhttps://www.bluetooth.com/specifications/assigned-numbers/) in the Bluetooth specification).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria/vendorid)*