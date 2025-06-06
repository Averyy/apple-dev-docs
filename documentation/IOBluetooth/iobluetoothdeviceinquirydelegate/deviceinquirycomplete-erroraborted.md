# deviceInquiryComplete(_:error:aborted:)

**Framework**: IOBluetooth  
**Kind**: method

**Availability**:
- macOS ?+

## Declaration

```swift
optional func deviceInquiryComplete(_ sender: IOBluetoothDeviceInquiry!, error: IOReturn, aborted: Bool)
```

#### Discussion

When the inquiry is completely stopped, this delegate method will be invoked. It will supply an error code value, kIOReturnSuccess if the inquiry stopped without problem, otherwise a non-kIOReturnSuccess error code will be supplied.

## Parameters

- `sender`: Inquiry object that sent this delegate message.
- `error`: Error code. kIOReturnSuccess if the inquiry completed without incident.
- `aborted`: TRUE if user called -stop on the inquiry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate/deviceinquirycomplete(_:error:aborted:))*