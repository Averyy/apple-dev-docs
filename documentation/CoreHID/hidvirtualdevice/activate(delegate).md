# activate(delegate:)

**Framework**: Core HID  
**Kind**: method  
**Role**: Instance Method

Activate a newly created virtual device to begin receiving notifications and enable functionality.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func activate(delegate: any HIDVirtualDeviceDelegate)
```

#### Discussion

Many functions won’t run, and notifications won’t be received using the [`HIDVirtualDeviceDelegate`](../hidvirtualdevicedelegate.md) until activate has run successfully. A device cannot be activated twice.

## Parameters

- `delegate`: The [`HIDVirtualDeviceDelegate`](../hidvirtualdevicedelegate.md) that receives incoming set/get report requests. Only one delegate is associated with the device, but many devices can be associated with the delegate.

## See Also

### Create a HID virtual device
- [init?(properties: HIDVirtualDevice.Properties)](./init%28properties%29.md)
  Creates a virtual HID device.
- [let deviceReference: HIDDeviceClient.DeviceReference](./devicereference.md)
  The reference to the virtual HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/activate(delegate:))*