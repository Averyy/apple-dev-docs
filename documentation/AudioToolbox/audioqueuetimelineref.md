# AudioQueueTimelineRef

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Defines an opaque data type that represents an audio queue timeline object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioQueueTimelineRef = OpaquePointer
```

```c
typedef struct OpaqueAudioQueueTimeline * AudioQueueTimelineRef;
```

## Discussion

You can use a timeline object to observe time discontinuities in the audio hardware device associated with an audio queue. A discontinuity is, for example, a period of silence when sound was expected. Causes of discontinuities include changes in device state or data processing overloads. See Technical Q&A 1467, [CoreAudio Overload Warnings](https://developer.apple.com/library/archive/qa/qa1467/_index.html#//apple_ref/doc/uid/DTS10003908). You query a timeline object by passing it as a parameter to the [`AudioQueueGetCurrentTime(_:_:_:_:)`](./audioqueuegetcurrenttime%28_,_,_,_%29.md) function.

## See Also

### Managing the Timeline
- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](./audioqueuecreatetimeline%28_,_%29.md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](./audioqueuedisposetimeline%28_,_%29.md)
  Disposes of an audio queue’s timeline object.
- [func AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audioqueuedevicegetcurrenttime%28_,_%29.md)
  Gets the current time of the audio hardware device associated with an audio queue.
- [func AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](./audioqueuedevicegetneareststarttime%28_,_,_%29.md)
  Gets the start time, for an audio hardware device, that is closest to a requested start time.
- [func AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](./audioqueuedevicetranslatetime%28_,_,_%29.md)
  Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.
- [func AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef?, UnsafeMutablePointer<AudioTimeStamp>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./audioqueuegetcurrenttime%28_,_,_,_%29.md)
  Gets the current audio queue time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuetimelineref)*