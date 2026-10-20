# CMOdometerOriginDevice

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

The device that the odometer sample originates from.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 10.15+
- visionOS 1.0+
- watchOS 8.4+

## Declaration

```swift
enum CMOdometerOriginDevice
```

```c
enum CMOdometerOriginDevice : NSInteger;
```

## Topics

### Device origins
- [CMOdometerOriginDevice.unknown](./cmodometerorigindevice/unknown.md)
  The origin of the odometer sample is unknown.
- [CMOdometerOriginDevice.local](./cmodometerorigindevice/local.md)
  The origin of the odometer sample comes from the same device that requests the sample.
- [CMOdometerOriginDevice.remote](./cmodometerorigindevice/remote.md)
  The origin of the odometer sample comes from a device that’s paired with the local device.
### Initializers
- [init?(rawValue: Int)](./cmodometerorigindevice/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the device
- [var originDevice: CMOdometerOriginDevice](./cmodometerdata/origindevice.md)
  The device that measures the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmodometerorigindevice)*