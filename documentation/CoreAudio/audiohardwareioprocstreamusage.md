# AudioHardwareIOProcStreamUsage

**Framework**: Core Audio  
**Kind**: struct

This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct AudioHardwareIOProcStreamUsage
```

#### Overview

## Topics

### Initializers
- [init(mIOProc: UnsafeMutableRawPointer, mNumberStreams: UInt32, mStreamIsOn: UInt32)](audiohardwareioprocstreamusage/init(mioproc:mnumberstreams:mstreamison:).md)
### Instance Properties
- [var mIOProc: UnsafeMutableRawPointer](audiohardwareioprocstreamusage/mioproc.md)
- [var mNumberStreams: UInt32](audiohardwareioprocstreamusage/mnumberstreams.md)
- [var mStreamIsOn: UInt32](audiohardwareioprocstreamusage/mstreamison.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct AudioObjectPropertyAddress](audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [struct AudioStreamRangedDescription](audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.
- [struct UnsafeMutableAudioBufferListPointer](unsafemutableaudiobufferlistpointer.md)
  A wrapper for a pointer to an `AudioBufferList`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareioprocstreamusage)*