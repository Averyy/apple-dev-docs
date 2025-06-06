# AudioQueueGetCurrentTime(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the current audio queue time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef?, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>?, _ outTimelineDiscontinuity: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAQ`: The audio queue whose current time you want to get.
- `inTimeline`: The audio queue timeline object to which timeline discontinuities are reported. Use   if the audio queue does not have an associated timeline object.
- `outTimeStamp`: On output, the current audio queue time. The   field represents audio queue time in terms of the audio queue sample rate, relative to when the queue started or will start.
- `outTimelineDiscontinuity`: A timeline discontinuity may occur, for example, if the sample rate is changed for the audio hardware device associated with an audio queue.

## See Also

- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](audioqueuecreatetimeline(_:_:).md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](audioqueuedisposetimeline(_:_:).md)
  Disposes of an audio queue’s timeline object.
- [func AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicegetcurrenttime(_:_:).md)
  Gets the current time of the audio hardware device associated with an audio queue.
- [func AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audioqueuedevicegetneareststarttime(_:_:_:).md)
  Gets the start time, for an audio hardware device, that is closest to a requested start time.
- [func AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicetranslatetime(_:_:_:).md)
  Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.
- [typealias AudioQueueTimelineRef](audioqueuetimelineref.md)
  Defines an opaque data type that represents an audio queue timeline object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuegetcurrenttime(_:_:_:_:))*