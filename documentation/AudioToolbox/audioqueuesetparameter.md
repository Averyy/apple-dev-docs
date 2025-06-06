# AudioQueueSetParameter(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets a playback audio queue parameter value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueSetParameter(_ inAQ: AudioQueueRef, _ inParamID: AudioQueueParameterID, _ inValue: AudioQueueParameterValue) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Use this function to change the settings for a playback audio queue directly. Changes take effect immediately. To set playback gain at the granularity of an audio queue buffer, use the [`AudioQueueEnqueueBufferWithParameters(_:_:_:_:_:_:_:_:_:_:)`](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md) function.

## Parameters

- `inAQ`: The playback audio queue that you want to set a parameter value on.
- `inParamID`: The ID of the parameter you want to set. In OS X v10.5, audio queues have one parameter available:  , which controls playback gain.  See  .
- `inValue`: The parameter value to set.

## See Also

- [func AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>?, UnsafePointer<AudioTimeStamp>?, UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md)
  Adds a buffer to the buffer queue of a playback audio queue object, specifying start time and other settings.
- [func AudioQueueGetParameter(AudioQueueRef, AudioQueueParameterID, UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus](audioqueuegetparameter(_:_:_:).md)
  Gets an audio queue parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuesetparameter(_:_:_:))*