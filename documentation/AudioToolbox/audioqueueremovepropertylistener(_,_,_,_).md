# AudioQueueRemovePropertyListener(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Removes a property listener callback from an audio queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueRemovePropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutableRawPointer?) -> OSStatus
```

```c
extern OSStatus AudioQueueRemovePropertyListener(AudioQueueRef inAQ, AudioQueuePropertyID inID, AudioQueuePropertyListenerProc inProc, void *inUserData);
```

## Return Value

A result code. See Result Codes.

## Parameters

- `inAQ`: The audio queue that you want to remove a property listener callback from.
- `inID`: The ID of the property whose changes you no longer want to respond to. See [`AudioQueuePropertyID`](./audioqueuepropertyid.md).
- `inProc`: The callback to be removed.
- `inUserData`: The same custom data for the property listener callback that you passed when calling [`AudioQueueAddPropertyListener(_:_:_:_:)`](./audioqueueaddpropertylistener%28_,_,_,_%29.md).

## See Also

### Manipulating Audio Queue Properties
- [func AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](./audioqueuegetproperty%28_,_,_,_%29.md)
  Gets an audio queue property value.
- [func AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeRawPointer, UInt32) -> OSStatus](./audioqueuesetproperty%28_,_,_,_%29.md)
  Sets an audio queue property value.
- [func AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus](./audioqueuegetpropertysize%28_,_,_%29.md)
  Gets the size of the value of an audio queue property.
- [func AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](./audioqueueaddpropertylistener%28_,_,_,_%29.md)
  Adds a property listener callback to an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueueremovepropertylistener(_:_:_:_:))*