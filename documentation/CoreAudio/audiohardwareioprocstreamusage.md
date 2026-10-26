# AudioHardwareIOProcStreamUsage

**Framework**: Core Audio  
**Kind**: struct  
**Role**: Structure

This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct AudioHardwareIOProcStreamUsage
```

```c
struct AudioHardwareIOProcStreamUsage;
```

#### Overview

- **`mIOProc`**: The IOProc whose stream usage is being specified.
- **`mNumberStreams`**: The number of streams being specified.
- **`mStreamIsOn`**: An array of UInt32’s whose length is specified by mNumberStreams. Each element of the array corresponds to a stream. A value of 0 means the stream is not to be enabled. Any other value means the stream is to be used.

## Topics

### Initializers
- [init(mIOProc: UnsafeMutableRawPointer, mNumberStreams: UInt32, mStreamIsOn: UInt32)](./audiohardwareioprocstreamusage/init%28mioproc,mnumberstreams,mstreamison%29.md)
### Instance Properties
- [var mIOProc: UnsafeMutableRawPointer](./audiohardwareioprocstreamusage/mioproc.md)
- [var mNumberStreams: UInt32](./audiohardwareioprocstreamusage/mnumberstreams.md)
- [var mStreamIsOn: UInt32](./audiohardwareioprocstreamusage/mstreamison.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct AudioObjectPropertyAddress](./audioobjectpropertyaddress.md)
  An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.
- [struct AudioStreamRangedDescription](./audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.
- [struct UnsafeMutableAudioBufferListPointer](./unsafemutableaudiobufferlistpointer.md)
  A wrapper for a pointer to an `AudioBufferList`.
- [AudioDriverPlugInHostInfo](./audiodriverpluginhostinfo.md)
- [AudioServerPlugInClientInfo](./audioserverpluginclientinfo.md)
- [AudioServerPlugInCustomPropertyInfo](./audioserverplugincustompropertyinfo.md)
- [AudioServerPlugInDriverInterface](./audioserverplugindriverinterface.md)
- [AudioServerPlugInHostInterface](./audioserverpluginhostinterface.md)
- [AudioServerPlugInIOCycleInfo](./audioserverpluginiocycleinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareioprocstreamusage)*