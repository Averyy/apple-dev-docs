# toCFAbsoluteTime()

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Converts an absolute time to a core-foundation absolute time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func toCFAbsoluteTime() -> CFAbsoluteTime
```

```c
extern CFAbsoluteTime SRAbsoluteTimeToCFAbsoluteTime(SRAbsoluteTime sr);
```

#### Return Value

The core-foundation absolute time.

## See Also

### Defining the Time Range
- [var from: SRAbsoluteTime](../srfetchrequest/from.md)
  Fetches sample information that occurs after this time.
- [var to: SRAbsoluteTime](../srfetchrequest/to.md)
  Fetches sample information that occurs before this time.
- [struct SRAbsoluteTime](../srabsolutetime.md)
  A value that describes when the system records the data.
- [static func current() -> SRAbsoluteTime](./current%28%29.md)
  Provides the current absolute time.
- [SRAbsoluteTimeFromCFAbsoluteTime](../srabsolutetimefromcfabsolutetime.md)
  Provides an absolute time equivalent to the argument core-foundation absolute time.
- [SRAbsoluteTimeFromContinuousTime](../srabsolutetimefromcontinuoustime.md)
  Provides an absolute time equivalent to the argument continuous time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srabsolutetime/tocfabsolutetime())*