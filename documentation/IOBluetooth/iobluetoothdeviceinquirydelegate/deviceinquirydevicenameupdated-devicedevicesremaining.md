# deviceInquiryDeviceNameUpdated(_:device:devicesRemaining:)

**Framework**: IOBluetooth  
**Kind**: method

**Availability**:
- macOS ?+

## Declaration

```swift
optional func deviceInquiryDeviceNameUpdated(_ sender: IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!, devicesRemaining: UInt32)
```

#### Discussion

A device name has been retrieved. Also indicates how many devices are left to be updated.

## Parameters

- `sender`: Inquiry object that sent this delegate message.
- `device`: IOBluetoothDevice that was updated.
- `devicesRemaining`: Number of devices remaining to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/deviceinquirydevicenameupdated(_:device:devicesremaining:))*