# SRAbsoluteTime

**Framework**: SensorKit  
**Kind**: struct

A value that describes when the system records the data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct SRAbsoluteTime
```

#### Discussion

This value tracks monotonically increasing device-specific time, unlike [`mach_continuous_time`](https://developer.apple.com/documentation/kernel/1646199-mach_continuous_time), which keeps tracking across reboots.

Although a fetch can query a [`device`](srfetchrequest/device.md) other than a phone (such as a paired watch), the framework consistently describes time according to the phone. Any fetch results from a paired watch are in the phone’s version of [`SRAbsoluteTime`](srabsolutetime.md).

## Topics

### Creating an Absolute Time
- [init(CFTimeInterval)](srabsolutetime/init(_:).md)
  Creates an absolute time from a raw value.
- [init(rawValue: CFTimeInterval)](srabsolutetime/init(rawvalue:).md)
  Creates an absolute time from a raw value.
### Accessing the Current Absolute Time
- [static func current() -> SRAbsoluteTime](srabsolutetime/current.md)
  Provides the current absolute time.
### Converting Absolute Times
- [func toCFAbsoluteTime() -> CFAbsoluteTime](srabsolutetime/tocfabsolutetime.md)
  Converts an absolute time to a core-foundation absolute time.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var from: SRAbsoluteTime](srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [var to: SRAbsoluteTime](srfetchrequest/to.md)
  Fetches sample information that occurs before this time.
- [static func current() -> SRAbsoluteTime](srabsolutetime/current.md)
  Provides the current absolute time.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](srabsolutetime/tocfabsolutetime.md)
  Converts an absolute time to a core-foundation absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srabsolutetime)*