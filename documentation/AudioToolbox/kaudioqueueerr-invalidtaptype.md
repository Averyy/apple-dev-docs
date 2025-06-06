# kAudioQueueErr_InvalidTapType

**Framework**: Audio Toolbox  
**Kind**: var

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioQueueErr_InvalidTapType: OSStatus { get }
```

## See Also

- [var kAudioQueueErr_BufferEmpty: OSStatus](kaudioqueueerr_bufferempty.md)
  The audio queue buffer is empty (that is, the `mAudioDataByteSize` field = `0`).
- [var kAudioQueueErr_BufferEnqueuedTwice: OSStatus](kaudioqueueerr_bufferenqueuedtwice.md)
- [var kAudioQueueErr_BufferInQueue: OSStatus](kaudioqueueerr_bufferinqueue.md)
  The audio queue buffer cannot be disposed of when it is enqueued.
- [var kAudioQueueErr_CannotStart: OSStatus](kaudioqueueerr_cannotstart.md)
  The audio queue has encountered a problem and cannot start.
- [var kAudioQueueErr_CodecNotFound: OSStatus](kaudioqueueerr_codecnotfound.md)
  The requested codec was not found.
- [var kAudioQueueErr_DisposalPending: OSStatus](kaudioqueueerr_disposalpending.md)
  The function cannot act on the audio queue because it is being asynchronously disposed of.
- [var kAudioQueueErr_EnqueueDuringReset: OSStatus](kaudioqueueerr_enqueueduringreset.md)
  During a call to the [`AudioQueueReset(_:)`](audioqueuereset(_:).md), [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md), or [`AudioQueueDispose(_:_:)`](audioqueuedispose(_:_:).md) functions, the system does not allow you to enqueue buffers.
- [var kAudioQueueErr_InvalidBuffer: OSStatus](kaudioqueueerr_invalidbuffer.md)
  The specified audio queue buffer does not belong to the specified audio queue.
- [var kAudioQueueErr_InvalidCodecAccess: OSStatus](kaudioqueueerr_invalidcodecaccess.md)
  The codec could not be accessed.
- [var kAudioQueueErr_InvalidDevice: OSStatus](kaudioqueueerr_invaliddevice.md)
  The specified audio hardware device could not be located.
- [var kAudioQueueErr_InvalidOfflineMode: OSStatus](kaudioqueueerr_invalidofflinemode.md)
  The operation requires the audio queue to be in offline mode but it isn’t, or vice versa.
- [var kAudioQueueErr_InvalidParameter: OSStatus](kaudioqueueerr_invalidparameter.md)
  The specified parameter ID is invalid.
- [var kAudioQueueErr_InvalidProperty: OSStatus](kaudioqueueerr_invalidproperty.md)
  The specified property ID is invalid.
- [var kAudioQueueErr_InvalidPropertySize: OSStatus](kaudioqueueerr_invalidpropertysize.md)
  The size of the specified property is invalid.
- [var kAudioQueueErr_InvalidPropertyValue: OSStatus](kaudioqueueerr_invalidpropertyvalue.md)
  The property value used is not valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidtaptype)*