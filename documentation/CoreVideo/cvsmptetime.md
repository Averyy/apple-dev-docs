# CVSMPTETime

**Framework**: Core Video  
**Kind**: struct

A structure for holding an SMPTE time.

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
struct CVSMPTETime
```

## Topics

### Initializers
- [init()](cvsmptetime/init.md)
- [init(subframes: Int16, subframeDivisor: Int16, counter: UInt32, type: UInt32, flags: UInt32, hours: Int16, minutes: Int16, seconds: Int16, frames: Int16)](cvsmptetime/init(subframes:subframedivisor:counter:type:flags:hours:minutes:seconds:frames:)-4yakl.md)
- [init(subframes: Int16, subframeDivisor: Int16, counter: UInt32, type: CVSMPTETimeType, flags: CVSMPTETimeFlags, hours: Int16, minutes: Int16, seconds: Int16, frames: Int16)](cvsmptetime/init(subframes:subframedivisor:counter:type:flags:hours:minutes:seconds:frames:)-7s092.md)
### Properties
- [var counter: UInt32](cvsmptetime/counter.md)
  The total number of messages received.
- [var flags: UInt32](cvsmptetime/flags.md)
  A set of flags that indicate the SMPTE state.
- [var frames: Int16](cvsmptetime/frames.md)
  The number of frames in the full message.
- [var hours: Int16](cvsmptetime/hours.md)
  The number of hours in the full message.
- [var minutes: Int16](cvsmptetime/minutes.md)
  The number of minutes in the full message.
- [var seconds: Int16](cvsmptetime/seconds.md)
  The number of seconds in the full message.
- [var subframeDivisor: Int16](cvsmptetime/subframedivisor.md)
  The number of subframes per frame (typically, 80).
- [var subframes: Int16](cvsmptetime/subframes.md)
  The number of subframes in the full message.
- [var type: UInt32](cvsmptetime/type.md)
  The kind of SMPTE time type.
### Instance Properties
- [var flagOptions: CVSMPTETimeFlags](cvsmptetime/flagoptions.md)
  `CVSMPTETimeFlags` representation of `CVSMPTETime.flags`
- [var typeOptions: CVSMPTETimeType](cvsmptetime/typeoptions.md)
  `CVSMPTETimeType` representation of `CVSMPTETime.type`

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CVTime](cvtime.md)
  A structure for reporting Core Video time values.
- [CVTimeStamp](cvtimestamp-api.md)
  A structure for representing a display timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvsmptetime)*