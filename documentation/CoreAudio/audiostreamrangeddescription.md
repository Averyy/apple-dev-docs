# AudioStreamRangedDescription

**Framework**: Core Audio  
**Kind**: struct

This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct AudioStreamRangedDescription
```

#### Overview

Note that this structure is only used to describe the the available formats for a stream. It is not used for the current format.

## Topics

### Initializers
- [init()](audiostreamrangeddescription/init.md)
- [init(mFormat: AudioStreamBasicDescription, mSampleRateRange: AudioValueRange)](audiostreamrangeddescription/init(mformat:msampleraterange:).md)
### Instance Properties
- [var mFormat: AudioStreamBasicDescription](audiostreamrangeddescription/mformat.md)
- [var mSampleRateRange: AudioValueRange](audiostreamrangeddescription/msampleraterange.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioHardwareIOProcStreamUsage](audiohardwareioprocstreamusage.md)
  This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.
- [struct AudioObjectPropertyAddress](audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [struct UnsafeMutableAudioBufferListPointer](unsafemutableaudiobufferlistpointer.md)
  A wrapper for a pointer to an `AudioBufferList`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiostreamrangeddescription)*