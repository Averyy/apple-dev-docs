# sourceDevice

**Framework**: SensorKit  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var sourceDevice: SRSourceDevice? { get }
```

#### Discussion

The source of the sample data

Represents the peripheral supplying data. Useful for distinguishing multiple source peripherals using a common device. Is nullable when no source information is available when providing sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchresult/sourcedevice)*