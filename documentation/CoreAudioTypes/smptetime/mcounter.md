# mCounter

**Framework**: Core Audio Types  
**Kind**: property

The total number of messages received. It takes 8 messages to carry a full SMPTE time code.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mCounter: UInt32
```

## See Also

- [var mFlags: SMPTETimeFlags](smptetime/mflags.md)
  A set of flags that indicate the SMPTE state (see `SMPTE Time Flags`).
- [var mFrames: Int16](smptetime/mframes.md)
  The value of the frames portion of the SMPTE time.
- [var mHours: Int16](smptetime/mhours.md)
  The value of the hours portion of the SMPTE time.
- [var mMinutes: Int16](smptetime/mminutes.md)
  The value of the minutes portion of the SMPTE time.
- [var mSeconds: Int16](smptetime/mseconds.md)
  The value of the seconds portion of the SMPTE time.
- [var mSubframeDivisor: Int16](smptetime/msubframedivisor.md)
  The number of subframes per video frame (typically 80).
- [var mSubframes: Int16](smptetime/msubframes.md)
  A subframe offset to the HH:MM:SS:FF time. You can use this field to position a time marker somewhere within the time span represented by a video frame, if necessary.
- [var mType: SMPTETimeType](smptetime/mtype.md)
  A SMPTE time type constant indicating the kind of SMPTE time used (see `SMPTE Timecode Types`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/smptetime/mcounter)*