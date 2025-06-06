# deviceInquiryStarted(_:)

**Framework**: IOBluetooth  
**Kind**: method

**Availability**:
- macOS ?+

## Declaration

```swift
optional func deviceInquiryStarted(_ sender: IOBluetoothDeviceInquiry!)
```

#### Discussion

This message will be delivered when the inquiry actually starts. Since the inquiry could be throttled, this message may not be received immediately after called -start.

## Parameters

- `sender`: Inquiry object that sent this delegate message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/deviceinquirystarted(_:))*