# AudioQueueGetParameter(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets an audio queue parameter value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueGetParameter(_ inAQ: AudioQueueRef, _ inParamID: AudioQueueParameterID, _ outValue: UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

You can access the current parameter values for an audio queue at any time with this function. An audio queue parameter value is the sum of settings applied at buffer granularity, using the [`AudioQueueEnqueueBufferWithParameters(_:_:_:_:_:_:_:_:_:_:)`](audioqueueenqueuebufferwithparameters(_:_:_:_:_:_:_:_:_:_:).md) function, and settings applied to the audio queue per se, using the [`AudioQueueSetParameter(_:_:_:)`](audioqueuesetparameter(_:_:_:).md) function.

## Parameters

- `inAQ`: The audio queue that you want to get a parameter value from.
- `inParamID`: The ID of the parameter whose value you want to get. In OS X v10.5, audio queues have one parameter available:  , which controls playback gain.  See 
- `outValue`: On output, points to the current value of the specified parameter.

## See Also

- [func AudioQueueSetParameter(AudioQueueRef, AudioQueueParameterID, AudioQueueParameterValue) -> OSStatus](audioqueuesetparameter(_:_:_:).md)
  Sets a playback audio queue parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuegetparameter(_:_:_:))*