# AudioQueueCreateTimeline(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a timeline object for an audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueCreateTimeline(_ inAQ: AudioQueueRef, _ outTimeline: UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Create a timeline object if you want to get timeline discontinuity information from an audio queue using the [`AudioQueueGetCurrentTime(_:_:_:_:)`](audioqueuegetcurrenttime(_:_:_:_:).md) function.

## Parameters

- `inAQ`: The audio queue to associate with the new timeline object.
- `outTimeline`: On output, the newly created timeline object.

## See Also

- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](audioqueuedisposetimeline(_:_:).md)
  Disposes of an audio queue’s timeline object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuecreatetimeline(_:_:))*