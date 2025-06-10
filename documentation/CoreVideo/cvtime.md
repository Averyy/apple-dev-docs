# CVTime

**Framework**: Core Video  
**Kind**: struct

A structure for reporting Core Video time values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CVTime
```

#### Overview

This structure is equivalent to the QuickTime `QTTime` structure.

## Topics

### Initializers
- [init()](cvtime/init.md)
- [init(timeValue: Int64, timeScale: Int32, flags: Int32)](cvtime/init(timevalue:timescale:flags:).md)
- [init(timeValue: Int64, timeScale: Int32)](cvtime/init(timevalue:timescale:).md)
  Initialize a valid CVTime value. Note: When `timeValue` has nonzero value, `timeScale` must be greater than 0.
### Properties
- [var flags: Int32](cvtime/flags.md)
  The flags associated with the `CVTime` value. See [`CVTime Values`](cvtime-values.md) for possible values. If `kCVTimeIsIndefinite` is set, you should not use any of the other fields in this structure.
- [var timeScale: Int32](cvtime/timescale.md)
  The time scale for this value.
- [var timeValue: Int64](cvtime/timevalue.md)
  The time value.
### Instance Properties
- [var flagOptions: CVTimeFlags](cvtime/flagoptions.md)
  `CVTimeFlags` representation of `CVTime.flags`
### Type Properties
- [static var indefinite: CVTime](cvtime/indefinite.md)
  CVTime with indefinite value
- [static var zero: CVTime](cvtime/zero.md)
  CVTime with 0 value

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CVTimeStamp](cvtimestamp-api.md)
  A structure for representing a display timestamp.
- [struct CVSMPTETime](cvsmptetime.md)
  A structure for holding an SMPTE time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtime)*