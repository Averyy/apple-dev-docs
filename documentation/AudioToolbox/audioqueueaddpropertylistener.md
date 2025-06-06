# AudioQueueAddPropertyListener(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Adds a property listener callback to an audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueAddPropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Use this function to let your application respond to property value changes in an audio queue. For example, say your application’s user interface has a button that acts as a Play/Stop toggle switch. When an audio file has finished playing, the audio queue stops and the value of the  `kAudioQueueProperty_IsRunning` property changes from `true` to `false`. You can use a property listener callback to update the button text appropriately.

## Parameters

- `inAQ`: The audio queue that you want to assign a property listener callback to.
- `inID`: The ID of the property whose changes you want to respond to. See  .
- `inProc`: The callback to be invoked when the property value changes.
- `inUserData`: Custom data for the property listener callback.

## See Also

- [func AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetproperty(_:_:_:_:).md)
  Gets an audio queue property value.
- [func AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeRawPointer, UInt32) -> OSStatus](audioqueuesetproperty(_:_:_:_:).md)
  Sets an audio queue property value.
- [func AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetpropertysize(_:_:_:).md)
  Gets the size of the value of an audio queue property.
- [func AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueremovepropertylistener(_:_:_:_:).md)
  Removes a property listener callback from an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueaddpropertylistener(_:_:_:_:))*