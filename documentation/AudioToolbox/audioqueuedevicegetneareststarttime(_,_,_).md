# AudioQueueDeviceGetNearestStartTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets the start time, for an audio hardware device, that is closest to a requested start time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueDeviceGetNearestStartTime(_ inAQ: AudioQueueRef, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus
```

```c
extern OSStatus AudioQueueDeviceGetNearestStartTime(AudioQueueRef inAQ, AudioTimeStamp *ioRequestedStartTime, UInt32 inFlags);
```

## Return Value

A result code. See Result Codes.

## Discussion

This function asks an audio queue’s associated device for a start time to use for recording or playback. The time returned will be equal to or later than the requested start time, depending on device and system factors. For example, the start time might be shifted to allow for aligning buffer access. The device must be running to use this function.

## Parameters

- `inAQ`: The audio queue whose associated audio hardware device’s start time you want to get.
- `ioRequestedStartTime`: On input, the requested start time. On output, the actual start time.
- `inFlags`: Reserved for future use. Pass `0`.

## See Also

### Managing the Timeline
- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](./audioqueuecreatetimeline%28_,_%29.md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](./audioqueuedisposetimeline%28_,_%29.md)
  Disposes of an audio queue’s timeline object.
- [func AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audioqueuedevicegetcurrenttime%28_,_%29.md)
  Gets the current time of the audio hardware device associated with an audio queue.
- [func AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audioqueuedevicetranslatetime%28_,_,_%29.md)
  Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.
- [func AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef?, UnsafeMutablePointer<AudioTimeStamp>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audioqueuegetcurrenttime%28_,_,_,_%29.md)
  Gets the current audio queue time.
- [typealias AudioQueueTimelineRef](./audioqueuetimelineref.md)
  Defines an opaque data type that represents an audio queue timeline object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuedevicegetneareststarttime(_:_:_:))*