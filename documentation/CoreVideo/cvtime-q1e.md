# CVTime

**Framework**: Core Video

A structure used for storing Core Video time values.

#### Overview

Core video uses the [`CVTime`](cvtime.md) and [`CVTimeStamp`](cvtimestamp.md) structures for storing Core Video time values. You use them to interact with the Core Video display link.

## Topics

### Inspecting the Host Clock
- [func CVGetCurrentHostTime() -> UInt64](cvgetcurrenthosttime().md)
  Returns the current system time.
- [func CVGetHostClockFrequency() -> Double](cvgethostclockfrequency().md)
  Returns the frequency of updates to the system time.
- [func CVGetHostClockMinimumTimeDelta() -> UInt32](cvgethostclockminimumtimedelta().md)
  Returns the smallest possible increment in the system time.
### Data Types
- [struct CVTime](cvtime.md)
  A structure for reporting Core Video time values.
- [CVTimeStamp](cvtimestamp-api.md)
  A structure for representing a display timestamp.
- [struct CVSMPTETime](cvsmptetime.md)
  A structure for holding an SMPTE time.
### Constants
- [CVTime Values](cvtime-values.md)
  Keys that represent Core Video time values.
### Enumerations
- [enum CVSMPTETimeType](cvsmptetimetype.md)
- [struct CVSMPTETimeFlags](cvsmptetimeflags.md)
- [struct CVTimeFlags](cvtimeflags.md)
- [struct CVTimeStampFlags](cvtimestampflags.md)

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [CVDisplayLink](cvdisplaylink-k0k.md)
  A high-priority thread that notifies your app when a given display will need each frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtime-q1e)*