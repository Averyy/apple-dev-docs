# deviceInquiryDeviceFound(_:device:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS

## Declaration

```swift
optional func deviceInquiryDeviceFound(_ sender: IOBluetoothDeviceInquiry!, device: IOBluetoothDevice!)
```

```objc
- (void) deviceInquiryDeviceFound:(IOBluetoothDeviceInquiry *) sender device:(IOBluetoothDevice *) device;
```

#### Discussion

A new device has been found. You do not need to retain the device - it will be held in the internal storage of the inquiry, and can be accessed later using -foundDevices.

## Parameters

- `sender`: Inquiry object that sent this delegate message.
- `device`: IOBluetoothDevice that was found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/deviceinquirydevicefound(_:device:))*