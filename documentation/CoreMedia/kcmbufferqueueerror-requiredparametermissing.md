# kCMBufferQueueError_RequiredParameterMissing

**Framework**: Core Media  
**Kind**: var

You failed to provide a valid value for a required parameter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCMBufferQueueError_RequiredParameterMissing: OSStatus { get }
```

## See Also

- [var kCMBufferQueueError_AllocationFailed: OSStatus](kcmbufferqueueerror_allocationfailed.md)
  The system failed to allocate memory.
- [var kCMBufferQueueError_InvalidCMBufferCallbacksStruct: OSStatus](kcmbufferqueueerror_invalidcmbuffercallbacksstruct.md)
  The format of a callbacks structure isn’t correct.
- [var kCMBufferQueueError_EnqueueAfterEndOfData: OSStatus](kcmbufferqueueerror_enqueueafterendofdata.md)
  You attempted to enqueue a buffer on a queue that disallows it.
- [var kCMBufferQueueError_QueueIsFull: OSStatus](kcmbufferqueueerror_queueisfull.md)
  You attempted to enqueue a buffer on a queue that’s full.
- [var kCMBufferQueueError_BadTriggerDuration: OSStatus](kcmbufferqueueerror_badtriggerduration.md)
  You specified an invalid trigger duration.
- [var kCMBufferQueueError_CannotModifyQueueFromTriggerCallback: OSStatus](kcmbufferqueueerror_cannotmodifyqueuefromtriggercallback.md)
  A trigger callback attempted to modify a queue.
- [var kCMBufferQueueError_InvalidTriggerCondition: OSStatus](kcmbufferqueueerror_invalidtriggercondition.md)
  You specified an invalid trigger condition.
- [var kCMBufferQueueError_InvalidTriggerToken: OSStatus](kcmbufferqueueerror_invalidtriggertoken.md)
  You specified a trigger token that isn’t a trigger currently associated with this queue.
- [var kCMBufferQueueError_InvalidBuffer: OSStatus](kcmbufferqueueerror_invalidbuffer.md)
  A buffer validation callback rejected the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmbufferqueueerror_requiredparametermissing)*