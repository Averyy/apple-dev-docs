# DeviceActivityData.Device

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

Device information for activity reporting.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Device
```

## Topics

### Identifying the device
- [var name: String?](./device-swift.struct/name.md)
  Access the name of the device set by the person.
- [var model: DeviceActivityData.Device.Model](./device-swift.struct/model-swift.property.md)
  Access the model of the device.
### Defining the device model
- [DeviceActivityData.Device.Model](./device-swift.struct/model-swift.enum.md)
  Device model types.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing device and user information
- [var user: DeviceActivityData.User](./user-swift.property.md)
  Access the person associated with the activity report.
- [var device: DeviceActivityData.Device](./device-swift.property.md)
  Access the device associated with the activity report.
- [DeviceActivityData.User](./user-swift.struct.md)
  Information about a person associated with an activity report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/device-swift.struct)*