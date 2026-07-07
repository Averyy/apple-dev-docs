# postNotificationWhenConsumed

**Framework**: Core Media  
**Kind**: property

Indicates that decode pipelines should post a notification when consuming the sample buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let postNotificationWhenConsumed: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMCustomNotificationInfo>
```

#### Discussion

This attachment is used at run time to request that a decode pipeline post [`kCMSampleBufferConsumerNotification_BufferConsumed`](kcmsamplebufferconsumernotification_bufferconsumed.md) notification when this sample buffer is consumed. The value for this key is used as the userInfo dictionary in the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/postnotificationwhenconsumed)*