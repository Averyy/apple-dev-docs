# AudioQueueDisposeTimeline(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Disposes of an audio queue’s timeline object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueDisposeTimeline(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Disposing of an audio queue automatically disposes of any associated resources, including a timeline object. Call this function only if you want to dispose of a timeline object and not the audio queue associated with it.

## Parameters

- `inAQ`: The audio queue associated with the timeline object you want to dispose of.
- `inTimeline`: The timeline object to dispose of.

## See Also

- [func AudioQueueDispose(AudioQueueRef, Bool) -> OSStatus](audioqueuedispose(_:_:).md)
  Disposes of an audio queue.
- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](audioqueuecreatetimeline(_:_:).md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicegetcurrenttime(_:_:).md)
  Gets the current time of the audio hardware device associated with an audio queue.
- [func AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audioqueuedevicegetneareststarttime(_:_:_:).md)
  Gets the start time, for an audio hardware device, that is closest to a requested start time.
- [func AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicetranslatetime(_:_:_:).md)
  Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.
- [func AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef?, UnsafeMutablePointer<AudioTimeStamp>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioqueuegetcurrenttime(_:_:_:_:).md)
  Gets the current audio queue time.
- [typealias AudioQueueTimelineRef](audioqueuetimelineref.md)
  Defines an opaque data type that represents an audio queue timeline object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuedisposetimeline(_:_:))*