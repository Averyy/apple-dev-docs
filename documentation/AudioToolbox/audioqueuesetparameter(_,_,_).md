# AudioQueueSetParameter(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioQueueSetParameter(AudioQueueRef inAQ, AudioQueueParameterID inParamID, AudioQueueParameterValue inValue);
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Use this function to change the settings for a playback audio queue directly. Changes take effect immediately. To set playback gain at the granularity of an audio queue buffer, use the [`AudioQueueEnqueueBufferWithParameters(_:_:_:_:_:_:_:_:_:_:)`](./audioqueueenqueuebufferwithparameters%28_,_,_,_,_,_,_,_,_,_%29.md) function.

## Parameters

- `inAQ`: The playback audio queue that you want to set a parameter value on.
- `inParamID`: The ID of the parameter you want to set. In OS X v10.5, audio queues have one parameter available: `kAudioQueueParam_Volume`, which controls playback gain.  See [Audio Queue Parameters](./api-1552626-audio-queue-parameters.md).
- `inValue`: The parameter value to set.

## See Also

### Related Documentation
- [func AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>?, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>?, UnsafePointer<AudioTimeStamp>?, UnsafeMutablePointer<AudioTimeStamp>?) -> OSStatus](./audioqueueenqueuebufferwithparameters%28_,_,_,_,_,_,_,_,_,_%29.md)
  Adds a buffer to the buffer queue of a playback audio queue object, specifying start time and other settings.
### Manipulating Audio Queue Parameters
- [func AudioQueueGetParameter(AudioQueueRef, AudioQueueParameterID, UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus](./audioqueuegetparameter%28_,_,_%29.md)
  Gets an audio queue parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuesetparameter(_:_:_:))*