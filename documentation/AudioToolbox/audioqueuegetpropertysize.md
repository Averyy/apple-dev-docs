# AudioQueueGetPropertySize(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the size of the value of an audio queue property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueGetPropertySize(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

## Parameters

- `inAQ`: The audio queue that has the property value whose size you want to get.
- `inID`: The ID of the property value whose size you want to get. See  .
- `outDataSize`: On output, the size of the requested property value.

## See Also

- [func AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetproperty(_:_:_:_:).md)
  Gets an audio queue property value.
- [func AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeRawPointer, UInt32) -> OSStatus](audioqueuesetproperty(_:_:_:_:).md)
  Sets an audio queue property value.
- [func AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueaddpropertylistener(_:_:_:_:).md)
  Adds a property listener callback to an audio queue.
- [func AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueremovepropertylistener(_:_:_:_:).md)
  Removes a property listener callback from an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuegetpropertysize(_:_:_:))*