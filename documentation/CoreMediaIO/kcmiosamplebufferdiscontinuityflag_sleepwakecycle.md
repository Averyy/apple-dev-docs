# kCMIOSampleBufferDiscontinuityFlag_SleepWakeCycle

**Framework**: Core Media I/O  
**Kind**: case  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
kCMIOSampleBufferDiscontinuityFlag_SleepWakeCycle
```

## Discussion

By increasing the duration of known good media;  this is a “soft” discontinuity, much like kCMIOSampleBufferDiscontinuityFlag_TimecodeDiscontinuity, meaning that the stream isn’t necessarily broken, but clients might want to force capture of all media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/kcmiosamplebufferdiscontinuityflag_sleepwakecycle)*