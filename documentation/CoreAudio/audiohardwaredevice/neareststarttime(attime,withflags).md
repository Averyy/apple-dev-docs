# nearestStartTime(atTime:withFlags:)

**Framework**: Core Audio  
**Kind**: method

Query the device to get a time equal to or later than the given time that is the best time to start IO.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func nearestStartTime(atTime timestamp: AudioTimeStamp, withFlags flags: UInt32 = 0) throws -> AudioTimeStamp
```

#### Return Value

An AudioTimeStamp containing a time equal to or later than the requested time, as dictated by the device’s constraints.

#### Discussion

The time that is returned is dictated by the constraints of the device and the system. For instance, the driver of a device that provides both audio and video data may only allow start times that coincide with the edge of a video frame. Also, if the device already has one or more active IOProcs, the start time will be shifted to the beginning of the next IO cycle so as not to cause discontinuities in the existing IOProcs. Another reason the start time may shift is to allow for aligning the buffer accesses in an optimal fashion. Note that the device must be running to use this function.

## Parameters

- `timestamp`: An AudioTimeStamp containing the requested start time.
- `flags`: A UInt32 containing flags that modify how this function behaves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/neareststarttime(attime:withflags:))*