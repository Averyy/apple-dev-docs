# kAudioQueueErr_CannotStart

**Framework**: Audio Toolbox  
**Kind**: var

The audio queue has encountered a problem and cannot start.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioQueueErr_CannotStart: OSStatus { get }
```

## See Also

- [var kAudioQueueErr_InvalidBuffer: OSStatus](kaudioqueueerr_invalidbuffer.md)
  The specified audio queue buffer does not belong to the specified audio queue.
- [var kAudioQueueErr_BufferEmpty: OSStatus](kaudioqueueerr_bufferempty.md)
  The audio queue buffer is empty (that is, the `mAudioDataByteSize` field = `0`).
- [var kAudioQueueErr_DisposalPending: OSStatus](kaudioqueueerr_disposalpending.md)
  The function cannot act on the audio queue because it is being asynchronously disposed of.
- [var kAudioQueueErr_InvalidProperty: OSStatus](kaudioqueueerr_invalidproperty.md)
  The specified property ID is invalid.
- [var kAudioQueueErr_InvalidPropertySize: OSStatus](kaudioqueueerr_invalidpropertysize.md)
  The size of the specified property is invalid.
- [var kAudioQueueErr_InvalidParameter: OSStatus](kaudioqueueerr_invalidparameter.md)
  The specified parameter ID is invalid.
- [var kAudioQueueErr_InvalidDevice: OSStatus](kaudioqueueerr_invaliddevice.md)
  The specified audio hardware device could not be located.
- [var kAudioQueueErr_BufferInQueue: OSStatus](kaudioqueueerr_bufferinqueue.md)
  The audio queue buffer cannot be disposed of when it is enqueued.
- [var kAudioQueueErr_InvalidRunState: OSStatus](kaudioqueueerr_invalidrunstate.md)
  The queue is running but the function can only operate on the queue when it is stopped, or vice versa.
- [var kAudioQueueErr_InvalidQueueType: OSStatus](kaudioqueueerr_invalidqueuetype.md)
  The queue is an input queue but the function can only operate on an output queue, or vice versa.
- [var kAudioQueueErr_Permissions: OSStatus](kaudioqueueerr_permissions.md)
  You do not have the required permissions to call the function.
- [var kAudioQueueErr_InvalidPropertyValue: OSStatus](kaudioqueueerr_invalidpropertyvalue.md)
  The property value used is not valid.
- [var kAudioQueueErr_PrimeTimedOut: OSStatus](kaudioqueueerr_primetimedout.md)
  During a call to the [`AudioQueuePrime(_:_:_:)`](audioqueueprime(_:_:_:).md) function, the audio queue’s audio converter failed to convert the requested number of sample frames.
- [var kAudioQueueErr_CodecNotFound: OSStatus](kaudioqueueerr_codecnotfound.md)
  The requested codec was not found.
- [var kAudioQueueErr_InvalidCodecAccess: OSStatus](kaudioqueueerr_invalidcodecaccess.md)
  The codec could not be accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_cannotstart)*