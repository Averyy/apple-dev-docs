# SRAbsoluteTimeFromCFAbsoluteTime

**Framework**: SensorKit  
**Kind**: func  
**Role**: Function

Provides an absolute time equivalent to the argument core-foundation absolute time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```c
extern SRAbsoluteTime SRAbsoluteTimeFromCFAbsoluteTime(CFAbsoluteTime cf);
```

#### Return Value

An absolute time equivalent to the argument core-foundatoin absolute time.

## Parameters

- `cf`: The core-foundation absolute time to convert.

## See Also

### Defining the Time Range
- [var from: SRAbsoluteTime](./srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [var to: SRAbsoluteTime](./srfetchrequest/to.md)
  Fetches sample information that occurs before this time.
- [struct SRAbsoluteTime](./srabsolutetime.md)
  A value that describes when the system records the data.
- [static func current() -> SRAbsoluteTime](./srabsolutetime/current%28%29.md)
  Provides the current absolute time.
- [SRAbsoluteTimeFromContinuousTime](./srabsolutetimefromcontinuoustime.md)
  Provides an absolute time equivalent to the argument continuous time.
- [func toCFAbsoluteTime() -> CFAbsoluteTime](./srabsolutetime/tocfabsolutetime%28%29.md)
  Converts an absolute time to a core-foundation absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srabsolutetimefromcfabsolutetime)*