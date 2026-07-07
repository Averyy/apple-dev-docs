# sourceDevice

**Framework**: SensorKit  
**Kind**: property

The source of the sample data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var sourceDevice: SRSourceDevice? { get }
```

#### Discussion

Represents the peripheral supplying data. Useful for distinguishing multiple source peripherals using a common device. Is nullable when no source information is available when providing sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchresponse/sourcedevice)*