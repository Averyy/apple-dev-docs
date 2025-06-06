# AudioQueueSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Sets an audio queue property value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueSetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inData: UnsafeRawPointer, _ inDataSize: UInt32) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAQ`: The audio queue that you want to set a property value on.
- `inID`: The ID of the property whose value you want to set. See  .
- `inData`: The property value to set.
- `inDataSize`: The size of the property data.

## See Also

- [func AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetproperty(_:_:_:_:).md)
  Gets an audio queue property value.
- [func AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetpropertysize(_:_:_:).md)
  Gets the size of the value of an audio queue property.
- [func AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueaddpropertylistener(_:_:_:_:).md)
  Adds a property listener callback to an audio queue.
- [func AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueremovepropertylistener(_:_:_:_:).md)
  Removes a property listener callback from an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuesetproperty(_:_:_:_:))*