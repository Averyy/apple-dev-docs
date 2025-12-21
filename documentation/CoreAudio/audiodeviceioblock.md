# AudioDeviceIOBlock

**Framework**: Core Audio  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias AudioDeviceIOBlock = (UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>) -> Void
```

#### Discussion

An AudioDeviceIOBlock is called by an AudioDevice to provide input data read from the device and collect output data to be written to the device for the current IO cycle.

## Parameters

- `inNow`: An AudioTimeStamp that indicates the IO cycle started. Note that this time   includes any scheduling latency that may have been incurred waking the   thread on which IO is being done.
- `inInputData`: An AudioBufferList containing the input data for the current IO cycle. For   streams that are disabled, the AudioBuffer’s mData field will be NULL but   the mDataByteSize field will still say how much data would have been there   if it was enabled. Note that the contents of this structure should never be   modified.
- `inInputTime`: An AudioTimeStamp that indicates the time at which the first frame in the   data was acquired from the hardware. If the device has no input streams, the   time stamp will be zeroed out.
- `outOutputData`: An AudioBufferList in which the output data for the current IO cycle is to   be placed. On entry, each AudioBuffer’s mDataByteSize field indicates the   maximum amount of data that can be placed in the buffer and the buffer’s   memory has been zeroed out. For formats where the number of bytes per packet   can vary (as with AC-3, for example), the client has to fill out on exit   each mDataByteSize field in each AudioBuffer with the amount of data that   was put in the buffer. Otherwise, the mDataByteSize field should not be   changed. For streams that are disabled, the AudioBuffer’s mData field will   be NULL but the mDataByteSize field will still say how much data would have   been there if it was enabled. Except as noted above, the contents of this   structure should not other wise be modified.
- `inOutputTime`: An AudioTimeStamp that indicates the time at which the first frame in the   data will be passed to the hardware. If the device has no output streams,   the time stamp will be zeroed out.

## See Also

- [typealias AudioClassID](audioclassid.md)
- [typealias AudioDeviceID](audiodeviceid.md)
- [typealias AudioDeviceIOProc](audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](audiodevicepropertylistenerproc.md)
- [typealias AudioHardwarePropertyID](audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](audioobjectid.md)
- [typealias AudioObjectPropertyElement](audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](audioobjectpropertyscope.md)
- [typealias AudioObjectPropertySelector](audioobjectpropertyselector.md)
- [typealias AudioStreamID](audiostreamid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceioblock)*