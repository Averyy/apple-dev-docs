# deviceInquiryUpdatingDeviceNamesStarted(_:devicesRemaining:)

**Framework**: IOBluetooth  
**Kind**: method

**Availability**:
- macOS ?+

## Declaration

```swift
optional func deviceInquiryUpdatingDeviceNamesStarted(_ sender: IOBluetoothDeviceInquiry!, devicesRemaining: UInt32)
```

#### Discussion

The inquiry has begun updating device names that were found during the search.

## Parameters

- `sender`: Inquiry object that sent this delegate message.
- `devicesRemaining`: Number of devices remaining to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/deviceinquiryupdatingdevicenamesstarted(_:devicesremaining:))*