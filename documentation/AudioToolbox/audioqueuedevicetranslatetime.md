# AudioQueueDeviceTranslateTime(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Converts the time for an audio queue’s associated audio hardware device from one time base representation to another.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueDeviceTranslateTime(_ inAQ: AudioQueueRef, _ inTime: UnsafePointer<AudioTimeStamp>, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

The device must be running for this function to provide a result. For an explanation of the various time base representations for an audio hardware device, see [`AudioTimeStamp`](https://developer.apple.com/documentation/CoreAudioTypes/AudioTimeStamp) in [`Core Audio Data Types`](https://developer.apple.com/documentation/CoreAudio/core-audio-data-types).

## Parameters

- `inAQ`: The audio queue associated with the device whose times are being translated.
- `inTime`: The time to be translated.
- `outTime`: On output, the translated time.

## See Also

- [func AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef?>) -> OSStatus](audioqueuecreatetimeline(_:_:).md)
  Creates a timeline object for an audio queue.
- [func AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus](audioqueuedisposetimeline(_:_:).md)
  Disposes of an audio queue’s timeline object.
- [func AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus](audioqueuedevicegetcurrenttime(_:_:).md)
  Gets the current time of the audio hardware device associated with an audio queue.
- [func AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus](audioqueuedevicegetneareststarttime(_:_:_:).md)
  Gets the start time, for an audio hardware device, that is closest to a requested start time.
- [func AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef?, UnsafeMutablePointer<AudioTimeStamp>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioqueuegetcurrenttime(_:_:_:_:).md)
  Gets the current audio queue time.
- [typealias AudioQueueTimelineRef](audioqueuetimelineref.md)
  Defines an opaque data type that represents an audio queue timeline object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuedevicetranslatetime(_:_:_:))*