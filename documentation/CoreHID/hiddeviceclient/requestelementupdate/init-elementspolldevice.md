# init(elements:pollDevice:)

**Framework**: Core HID  
**Kind**: init

Creates a request element update.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(elements: [HIDElement], pollDevice: Bool = true)
```

## Parameters

- `elements`: The elements used to request updates.
- `pollDevice`: Whether the device should be polled for new updates, or if the most recently received values can be returned without device interaction. If true, one or more get report requests are issued to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/requestelementupdate/init(elements:polldevice:))*