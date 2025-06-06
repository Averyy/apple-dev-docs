# Anonymous

**Framework**: Audio Toolbox

## Topics

### Constants
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
- [var kAudioQueueErr_InvalidQueueType: OSStatus](kaudioqueueerr_invalidqueuetype.md)
  The queue is an input queue but the function can only operate on an output queue, or vice versa.
- [var kAudioQueueErr_InvalidRunState: OSStatus](kaudioqueueerr_invalidrunstate.md)
  The queue is running but the function can only operate on the queue when it is stopped, or vice versa.
- [var kAudioQueueErr_InvalidTapContext: OSStatus](kaudioqueueerr_invalidtapcontext.md)
- [var kAudioQueueErr_InvalidTapType: OSStatus](kaudioqueueerr_invalidtaptype.md)
- [var kAudioQueueErr_Permissions: OSStatus](kaudioqueueerr_permissions.md)
  You do not have the required permissions to call the function.
- [var kAudioQueueErr_PrimeTimedOut: OSStatus](kaudioqueueerr_primetimedout.md)
  During a call to the [`AudioQueuePrime(_:_:_:)`](audioqueueprime(_:_:_:).md) function, the audio queue’s audio converter failed to convert the requested number of sample frames.
- [var kAudioQueueErr_QueueInvalidated: OSStatus](kaudioqueueerr_queueinvalidated.md)
  In iOS, the audio server has exited, causing the audio queue to become invalid.
- [var kAudioQueueErr_RecordUnderrun: OSStatus](kaudioqueueerr_recordunderrun.md)
  During recording, data was lost because there was no enqueued buffer to store it in.
- [var kAudioQueueErr_TooManyTaps: OSStatus](kaudioqueueerr_toomanytaps.md)
- [var kAudioQueueErr_CannotStartYet: OSStatus](kaudioqueueerr_cannotstartyet.md)

## See Also

- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [Audio Queue Time Pitch Algorithms](1552630-audio-queue-time-pitch-algorithm.md)
- [Audio Queue Property IDs](1552629-audio-queue-property-ids.md)
- [Audio Queue Property IDs](1618733-audio-queue-property-ids.md)
- [Audio Queue Hardware Codec Policy](1618727-audio-queue-hardware-codec-polic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous)*