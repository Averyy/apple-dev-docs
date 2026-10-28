# AudioQueueSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioQueueSetProperty(AudioQueueRef inAQ, AudioQueuePropertyID inID, const void *inData, UInt32 inDataSize);
```

## Return Value

A result code. See Result Codes.

## Parameters

- `inAQ`: The audio queue that you want to set a property value on.
- `inID`: The ID of the property whose value you want to set. See [`AudioQueuePropertyID`](./audioqueuepropertyid.md).
- `inData`: The property value to set.
- `inDataSize`: The size of the property data.

## See Also

### Manipulating Audio Queue Properties
- [func AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](./audioqueuegetproperty%28_,_,_,_%29.md)
  Gets an audio queue property value.
- [func AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus](./audioqueuegetpropertysize%28_,_,_%29.md)
  Gets the size of the value of an audio queue property.
- [func AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audioqueueaddpropertylistener%28_,_,_,_%29.md)
  Adds a property listener callback to an audio queue.
- [func AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audioqueueremovepropertylistener%28_,_,_,_%29.md)
  Removes a property listener callback from an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuesetproperty(_:_:_:_:))*