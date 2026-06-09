# headphoneMotion

**Framework**: SensorKit  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static let headphoneMotion: SRSensor
```

#### Discussion

Sensor stream for headphone motion collection

This stream stores samples about headphone motion including:

- acceleration measured by the device’s accelerometer
- rotation rate measured by the device’s gyroscope
- altitude

Fetches from this stream return objects of type \c NSArray<CMRecordedDeviceMotion *> * as defined in the CoreMotion framework


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensor/headphonemotion)*