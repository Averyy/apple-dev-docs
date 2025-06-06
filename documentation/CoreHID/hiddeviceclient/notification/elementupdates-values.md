# HIDDeviceClient.Notification.elementUpdates(values:)

**Framework**: Core HID  
**Kind**: case

A notification that elements of the device were updated.

**Availability**:
- macOS 15.0+

## Declaration

```swift
case elementUpdates(values: [HIDElement.Value])
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Discussion

This is typically received in response to input reports, and is another way to receive the data in a different format than [`HIDDeviceClient.Notification.inputReport(id:data:timestamp:)`](hiddeviceclient/notification/inputreport(id:data:timestamp:).md).

## Parameters

- `values`: The updated values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/notification/elementupdates(values:))*