# subdevices

**Framework**: Core Audio  
**Kind**: property

An array of AudioHardwareClocks representing all the devices and clocks, active or inactive, contained in the aggregate device. The order of the items in the array is significant and is used to determine the order of the streams of the aggregate device.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var subdevices: [AudioHardwareClock] { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareaggregatedevice/subdevices)*