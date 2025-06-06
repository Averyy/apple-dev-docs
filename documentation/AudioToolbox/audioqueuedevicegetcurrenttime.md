# AudioQueueDeviceGetCurrentTime(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the current time of the audio hardware device associated with an audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueDeviceGetCurrentTime(_ inAQ: AudioQueueRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This function returns a value whether or not the audio hardware device associated with the audio queue is running. The similar `AudioDeviceGetCurrentTime` function, declared in the `AudioHardware.h` header file, returns an error in this case.

## Parameters

- `inAQ`: The audio queue whose associated audio device is to be queried.
- `outTimeStamp`: On output, the current time of the audio hardware device associated with the audio queue. If the device is not running, the only valid field in the audio timestamp structure is  .

## See Also

- [func AudioDeviceGetCurrentTime(_ inDevice: AudioObjectID, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](../CoreAudio/AudioDeviceGetCurrentTime(_:_:).md)
- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](audioqueuecreatetimeline(_:_:).md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](audioqueuedisposetimeline(_:_:).md)
  Disposes of an audio queue’s timeline object.
- [func AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audioqueuedevicegetneareststarttime(_:_:_:).md)
  Gets the start time, for an audio hardware device, that is closest to a requested start time.
- [func AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicetranslatetime(_:_:_:).md)
  Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.
- [func AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef?, UnsafeMutablePointer<AudioTimeStamp>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioqueuegetcurrenttime(_:_:_:_:).md)
  Gets the current audio queue time.
- [typealias AudioQueueTimelineRef](audioqueuetimelineref.md)
  Defines an opaque data type that represents an audio queue timeline object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuedevicegetcurrenttime(_:_:))*