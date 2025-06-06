# kCMSampleBufferConsumerNotification_BufferConsumed

**Framework**: Core Media  
**Kind**: var

Optionally posted when a sample buffer is consumed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMSampleBufferConsumerNotification_BufferConsumed: CFString
```

#### Discussion

If a sample buffer has a value for the [`kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed`](kcmsamplebufferattachmentkey_postnotificationwhenconsumed.md) attachment, an object that consumes the sample buffer should post this notification with itself as the notifying object and the attachment value as the `userInfo` dictionary.

## See Also

- [let kCMSampleBufferNotification_DataBecameReady: CFString](kcmsamplebuffernotification_databecameready.md)
  Posted on a sample buffer by the [`CMSampleBufferSetDataReady(_:)`](cmsamplebuffersetdataready(_:).md) function when the buffer becomes ready.
- [let kCMSampleBufferNotification_DataFailed: CFString](kcmsamplebuffernotification_datafailed.md)
- [let kCMSampleBufferNotificationParameter_OSStatus: CFString](kcmsamplebuffernotificationparameter_osstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconsumernotification_bufferconsumed)*