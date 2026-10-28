# SRAbsoluteTime

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

A value that describes when the system records the data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct SRAbsoluteTime
```

```c
typedef CFTimeInterval SRAbsoluteTime;
```

## Discussion

This value tracks monotonically increasing device-specific time, unlike [`mach_continuous_time`](../kernel/api-1646199-mach_continuous_time.md), which keeps tracking across reboots.

Although a fetch can query a [`device`](./srfetchrequest/device.md) other than a phone (such as a paired watch), the framework consistently describes time according to the phone. Any fetch results from a paired watch are in the phone’s version of [`SRAbsoluteTime`](./srabsolutetime.md).

## Topics

### Creating an Absolute Time
- [init(CFTimeInterval)](./srabsolutetime/init%28_%29.md)
  Creates an absolute time from a raw value.
- [init(rawValue: CFTimeInterval)](./srabsolutetime/init%28rawvalue%29.md)
  Creates an absolute time from a raw value.
### Accessing the Current Absolute Time
- [static func current() -> SRAbsoluteTime](./srabsolutetime/current%28%29.md)
  Provides the current absolute time.
### Converting Absolute Times
- [func toCFAbsoluteTime() -> CFAbsoluteTime](./srabsolutetime/tocfabsolutetime%28%29.md)
  Converts an absolute time to a core-foundation absolute time.
- [SRAbsoluteTimeFromCFAbsoluteTime](./srabsolutetimefromcfabsolutetime.md)
  Provides an absolute time equivalent to the argument core-foundation absolute time.
- [SRAbsoluteTimeFromContinuousTime](./srabsolutetimefromcontinuoustime.md)
  Provides an absolute time equivalent to the argument continuous time.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining the Time Range
- [var from: SRAbsoluteTime](./srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [var to: SRAbsoluteTime](./srfetchrequest/to.md)
  Fetches sample information that occurs before this time.
- [static func current() -> SRAbsoluteTime](./srabsolutetime/current%28%29.md)
  Provides the current absolute time.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](./srabsolutetime/tocfabsolutetime%28%29.md)
  Converts an absolute time to a core-foundation absolute time.
- [SRAbsoluteTimeFromCFAbsoluteTime](./srabsolutetimefromcfabsolutetime.md)
  Provides an absolute time equivalent to the argument core-foundation absolute time.
- [SRAbsoluteTimeFromContinuousTime](./srabsolutetimefromcontinuoustime.md)
  Provides an absolute time equivalent to the argument continuous time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srabsolutetime)*