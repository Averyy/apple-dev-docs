# current()

**Framework**: SensorKit  
**Kind**: method

Provides the current absolute time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static func current() -> SRAbsoluteTime
```

#### Return Value

The absolute time of the current device.

#### Discussion

Each device has their own absolute time. This function returns the absolute time of the [`current`](srdevice/current.md) device.

## See Also

- [var from: SRAbsoluteTime](srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [var to: SRAbsoluteTime](srfetchrequest/to.md)
  Fetches sample information that occurs before this time.
- [struct SRAbsoluteTime](srabsolutetime.md)
  A value that describes when the system records the data.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](srabsolutetime/tocfabsolutetime.md)
  Converts an absolute time to a core-foundation absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srabsolutetime/current())*